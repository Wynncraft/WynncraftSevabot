#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple player server checking module using the Wynncraft API
"""
import urllib2
import sys
import json

# Make sure we have a player argument passed
if(len(sys.argv) > 1):
	# Set Headers to emulate a client request
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	try:
		# Call the Wynncraft API and set it as a json object
		req = urllib2.Request("http://api.wynncraft.com/public_api.php?action=playerStats&command=" + sys.argv[1], headers=hdr)
		opener = urllib2.build_opener()
		f = opener.open(req)
		json = json.loads(f.read())

		# Check if the player is online or not
		if(json['current_server'] == 'null' ):
			print sys.argv[1], ' is currently offline'
		else:
			print sys.argv[1], ' is currently on server ', json['current_server'], '.'
	except:
		# Handle status 400 from the API for players that don't exist in the database
		print 'Error: ', sys.argv[1], '  has never been on the Wynncraft Network.'
else:
	# If a player argument is missing tell the user
	print 'Error: Player argument needed. Try !whereis <player> instead.'
