# personal-scripts
This is a collection of all my personal scripts over the years.

++++++

**mcast:**
This is written to be a (full featured?) shoutcast client using mplayer.

**Requirements:**

mplayer

bash completion

zenity is optional, but required should you need the ui option.


**Installation of completion file:**
```
cp ./Bash/MCast/mcast.bash_completion /etc/bash_completion.d/mcast

```

**Usage:**
```
add [title] [url] - Adds a shoutcast stream for playback later
del [title]       - Delete an existing shoutcast stream
last              - Plays the last used radio station
list              - List all stored shoutcast streams
play [title]      - Play a stored shoutcast stream
ui                - Start a zenity frontend
url [id]          - Adds a shoutcast stream using the station ID
usage             - This help screen.
```

**Finding the shoutcast stationId:**
In a browser navigate to [shoutcast.com](http://www.shoutcast.com) and find a station you like. Hover over the download button and you will notice the url it wants to go to is something like this
```
yp.shoutcast.com/sbin/tunein-station.pls?id=558051
```

Those last 6 digits are the station ID

++++++

**GETTIT.PY:**
This is a python script I've modified. Source unknown/forgot.

The original couldn't handle album links, which I included. 

Yes, the script does use two different methods for downloading files, a urlretrieve for individual images, and Imgur API call for albums.

This is due to worrying about hitting API limits. But probably unnecessary. I'll fix it whenever.

**Requirements:**

Python Modules: requests, urllib urllib.request, re, os, sys, time, imgurpython

gettit.py [subreddit] [subreddit]...

This then cycles through the first 100 posts (configurable) on the what's hot list of that subreddit, and downloads the image, if it's from imgur and if it reaches a score threshold of 10 (also configurable).

**List of wanted improvements:**

- [ ] Command line option to set post limit and score limits

- [ ] Command line switch to be able to toggle between the sort methods (new / hot / top / rising)

- [ ] Ability to handle tumblr and gfycat links.

++++++

**history_stats:**
Fun bash one-liner to get a quick status of your bash history, giving usage percentages. 

This defaults to 60 lines, but can be set as an argument

**Usage:**
history_stats [number of lines]


