#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tweets lines from Poe's Tell-Tale Heart, Raven, and Fall of the House of Usher

import tweepy, time

CONSUMER_KEY = 'xxxxxxxxxxxxxxx' # To get this stuff, sign in at https://dev.twitter.com/ and Create a New Application
CONSUMER_SECRET = 'xxxxxxxxxxxxxxx' # Make sure access level is Read And Write in the Settings tab
ACCESS_KEY = 'xxxxxxxxxxxxxxx' # Create a new Access Token
ACCESS_SECRET = 'xxxxxxxxxxxxxxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('poe-lines.txt','r')
f=filename.readlines()
filename.close()

for line in f: 
    api.update_status(line)
    print line
    time.sleep(3600) # Sleep for 1 hour (3600 seconds)
