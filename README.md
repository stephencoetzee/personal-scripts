# personal-scripts
This is a collection of all my personal scripts over the years.

_GETTIT.PY:_
This is a python script I've modified. Source unknown/forgot.

The original couldn't handle album links, which I included. 

Yes, the script does use two different methods for downloading files, a urlretrieve for individual images, and Imgur API call for albums.

This is due to worrying about hitting API limits. But probably unnecessary. I'll fix it whenever.

_Requirements:_

Python Modules: requests, urllib urllib.request, re, os, sys, time, imgurpython

_Usage:_

gettit.py [subreddit] [subreddit]...

This then cycles through the first 100 posts (configurable) on the what's hot list of that subreddit, and downloads the image, if it's from imgur and if it reaches a score threshold of 10 (also configurable).

_List of wanted improvements:_

Command line option to set post limit and score limits

Command line switch to be able to toggle between the sort methods (new / hot / top / rising)

Ability to handle tumblr and gfycat links.
