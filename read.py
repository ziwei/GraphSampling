#!/usr/bin/python
import re
import depend

def readsample(filename1) :
 sampleList = []

 #filename1 = "samplelist.txt"

 i = 0
 for line in open(filename1, "r") :
  sampleList.append([])
  linestr = line.split("\n")[0]
  name = linestr.split(";")[0]
  degree = linestr.split(";")[1]
  sampleList[i].append(str(name))
  sampleList[i].append(str(degree))
  i = i + 1

 return sampleList

def readfriend(filename2) :
 friendList = []

 #filename2 = "friendlist.txt"

 j = 0
 for line in open(filename2, "r") :
  friendList.append([])
  q = 0
  for name in line.split(";") :
   friendList[j].append(str(name))
   q = q + 1
  j = j + 1
 
 return friendList
