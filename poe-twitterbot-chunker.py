#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @robincamille

# Split up a text into tweetable chunks. This script
# puts sentences from source text into a TXT file where each sentence
# in a new line. If any sentence is over 140 chars, the script marks it
# with SPLIT. You'll have to go through your lines manually to split up these
# sentences. You could do this programmatically, too, but it often reads better
# if you have some editorial control.

import re, nltk.data, string
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

filename=open('filename.txt','r') #
f=filename.read()
filename.close()

w=open('lines.txt','w')

fsent = sent_detector.tokenize(f.strip())

for sent in fsent:
    if len(sent) <= 140:
        w.write(sent)
        w.write("\n")
    elif len(sent) > 141:
        w.write("SPLIT ")
        w.write(sent)
        w.write("/n")
    else:
        pass

print "DONESIES"

w.close()
