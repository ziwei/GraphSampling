#!/usr/bin/python

import urllib2
import re
import random
import sys

def rw(from_user):
	api_key = '290309f59e849427d314b2c91aaf818b'
	command = "http://ws.audioscrobbler.com/2.0/?method=user.getfriends&user="+from_user+"&limit=500&page=1&api_key="+api_key
	data = urllib2.urlopen(command).read()
	degree = int(re.search('total="(\d+)"', data).group(1))
	n = random.uniform(0, degree)
	if n == degree :
	 n = n - 1
	print "init n " + str(n)
	friends = []
	if degree == 0 :
		dest_user = None
		friends = []
	elif degree <= 500 :
	 	friends = re.findall("<name>(.*)</name>", data)
		listlen = len(friends)
       		print "list size " + str(listlen)
       		print "n  "+ str(n) + " degree" + str(degree)
	else :
		page = int(n/500) + 1
	 	n = int(n%500)
	 	command = "http://ws.audioscrobbler.com/2.0/?method=user.getfriends&user="+from_user+"&limit=500&page="+str(page)+"&api_key="+api_key
	 	data = urllib2.urlopen(command).read()
	 	currentfriends = re.findall("<name>(.*)</name>", data)
		listlen = len(currentfriends)
		print "list size " + str(listlen)
		print "n  "+ str(n) + " degree" + str(degree)
		for i in range(1, int(degree/500) + 1) :
		 command = "http://ws.audioscrobbler.com/2.0/?method=user.getfriends&user="+from_user+"&limit=500&page="+str(i)+"&api_key="+api_key
		 data = urllib2.urlopen(command).read()
	 	 friends = friends + re.findall("<name>(.*)</name>", data)
	return (dest_user, friends)
