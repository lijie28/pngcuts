#!/usr/bin/env python
#encoding=utf-8
import cStringIO, urllib2
from PIL import Image
url = 'http://www.jb51.net/images/logo.gif'
file = urllib2.urlopen(url)
tmpIm = cStringIO.StringIO(file.read())
im = Image.open(tmpIm)
print im.format, im.size, im.mode