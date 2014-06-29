#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple player count module
"""
import urllib2
import json

# Set Headers to emulate a client request
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# Call the Wynncraft API and set it as a json object
req = urllib2.Request("http://api.wynncraft.com/public_api.php?action=onlinePlayersSum", headers=hdr)
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())

# Output response
print 'There are currently ', json['players_online'], ' players online on the Wynncraft Network.'
