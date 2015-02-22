#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import datetime

try:
	r = requests.get("http://photography.nationalgeographic.com/photography/photo-of-the-day/")

	body = r.text
	soup = BeautifulSoup(body)
	img_tag = soup.findAll('img',attrs={'width':"990" ,'height':"743"})
	picture_url = img_tag[0].attrs['src']

	FILENAME = "PictureOfTheDay-%s.jpg" % str(datetime.date.today())

	picture_url_request = requests.get('http:' + picture_url)
	picture_file_handle = open(FILENAME,'w')
	for chunk in picture_url_request.iter_content(chunk_size=1024):
	    if chunk:
	        picture_file_handle.write(chunk)
	        picture_file_handle.flush()
	picture_file_handle.close()
	print "NatGeo Picture Of The Day downloaded to %s" % FILENAME
except Exception,e:
	print "Exception occoured ", e