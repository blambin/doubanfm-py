#!/usr/bin/env python
#coding:utf-8

import urllib2
import sys,urllib
import re,json,os

def printheader(*args):
  print "*******************"
  print "* douban Radio * "
  for i in range(len(args)):
    print "args[", i, "]=", args[i]
  print "*******************"
  return

printheader()

#---循環運行下載回來的歌單--begin---
while True:
  listcontent = ""
  for line in urllib2.urlopen('http://douban.fm/j/mine/playlist?type=n&channel=0'):
    
    listcontent = listcontent + line
    contents = json.loads(listcontent)
    urls=[]
  for song in contents["song"]:
   
    urls.append(song["url"])
  print "Playlist:"
  for url in urls:
    print " Song : " + url
    cmd = "mplayer " + url  
    os.system(cmd)
#---循環運行下載回來的歌單--end----
