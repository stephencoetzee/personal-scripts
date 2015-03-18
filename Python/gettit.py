#!/usr/bin/python
import requests, urllib, urllib.request, re
import os, sys, time
from imgurpython import ImgurClient

counter = 0

def getPosts(subreddit, postLimit):
	url = 'http://www.reddit.com/r/' + subreddit + '/.json?limit=' + str(postLimit)
	headers = {
		'User-Agent': 'Reddit Image Scraper 1.1'
	}
	r = requests.get(url, headers=headers)
	if r.status_code == requests.codes.ok:
		data = r.json()
		print('Sleeping for 3 seconds...\n')
		time.sleep(3)
		return data['data']['children']
	else:
		print('Sorry, but there was an error retrieving the subreddit\'s data!')
		return None

def saveImages(posts, scoreLimit, save_dir='scraped_wallpapers'):
	for post in posts:
		url = post['data']['url']
		score = post['data']['score']
		title = post['data']['title']
		if 'http://i.imgur.com' in url and score > scoreLimit:
			saveImage(url, title, save_dir)
		elif 'http://imgur.com/a/' in url and score > scoreLimit: 
			saveAlbum(url, save_dir)
 
def saveImage(url, title, save_dir):
	global counter
	save_dir = makeSaveDir(save_dir)
	title = re.sub(r'\W+', '', title)
	dot_location = url.rfind('.')
	filename = (save_dir + title.replace('/', ':') + url[dot_location: dot_location + 4]).encode('utf-8')
	if not os.path.exists(filename):
		print('Saving ' + filename.decode('utf-8') + '!\n')
		counter += 1
		urllib.request.urlretrieve(url, filename)

def saveAlbum(url, save_dir):
	#Sign up for an imgur api here (Oauth with no callback) and paste your keys here
	client_id = 'REDACTED'
	client_secret = 'REDACTED'
	icounter = 0
	
	client = ImgurClient(client_id, client_secret)
	
	if '/#0' in url:
	    url = url[:-3]
	
	album_id = url.split('/')[-1]

	if '#' in album_id:
	    album_id = album_id[:5]
	
	print(url)
	print(album_id)

	album_title = client.get_album(album_id).title
	if album_title is None:
		album_title = 'Untitled ' + album_id
	
	print(album_title)

	album_title = album_title.replace(' ', '')
	album_title = re.sub(r'\W+', '', album_title)

	
	save_dir = save_dir + '/' + album_title
	if not os.path.exists(save_dir):
		os.makedirs(save_dir)

	for image in client.get_album_images(album_id):
		icounter += 1
		title = album_title + '_' + str(icounter)
		saveImage(image.link, title, save_dir)

def makeSaveDir(dir):
	if not os.path.exists(dir):
		 os.makedirs(dir)
	return dir + '/'

def downloadImagesFromReddit(subreddits, postLimit=100, scoreLimit=10):
	for subreddit in subreddits:
		posts = getPosts(subreddit, postLimit)
		saveImages(posts, scoreLimit, subreddit.lower())
	print(str(counter) + ' images have been scraped!')


def main():
    if len(sys.argv) > 1:
	    downloadImagesFromReddit(sys.argv[1:])
    else:
	    downloadImagesFromReddit([
		    'wallpapers'
	    ])

if __name__ == '__main__':
	main()
