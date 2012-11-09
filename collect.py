#!/usr/bin/python
import re

import  RW

friendList = 0
prename = 0
filename1 = "samplelist.txt"
filename2 = "friendlist.txt"
(currentname, friendList) = RW.rw("IscariotCX667")

for i in range(1,10000) :
  (nextname, friendList) = RW.rw(currentname)
  if nextname != None :
   file1 = open(filename1, "a")
   file1.write(currentname+";"+str(len(friendList))+"\n")
   file2 = open(filename2, "a")
   for j in range(0, len(friendList)) :
    file2.write(friendList[j] + ";")
   file2.write("\n")
   prename = currentname
  else :
   (nextname, friendList) = RW.rw(prename)

  currentname = nextname
  print "Run " + str(i)


