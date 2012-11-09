#!/usr/bin/python
import re

def thinningsample(sampleList, theta, offset):
 newsampleList = []

 i = 0
 j = 0
 for [name, degree] in sampleList :
  if i % theta == offset :
   newsampleList.append([])
   newsampleList[j].append(name)
   newsampleList[j].append(degree)
   j = j + 1
  i = i + 1
 return newsampleList

def thinningfriend(friendList, theta, offset):
 newfriendList = []

 i = 0
 j = 0
 for line in friendList :
  if i % theta == offset :
   newfriendList.append([])
   for name in line :
    newfriendList[j].append(name)
   j = j + 1
  i = i + 1
 return newfriendList





















 
