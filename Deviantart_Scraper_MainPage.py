from bs4 import BeautifulSoup
import urllib.request
import urllib
import re
import os
from datetime import datetime


c = 0
url = "http://www.deviantart.com/browse/all/?offset="
count = 0
path = "C:/Users/luisdeolpy/Pictures/Deviantart_Script/" + \
	datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(":", "-")
os.makedirs(path)

while (c < 101):
	html = urllib.request.urlopen(url + str(c)).read()
	sopa = BeautifulSoup(html, "html.parser")
	for img in sopa.find_all("img", class_=""):
		if img.find(src=re.compile("/avatars")):
			pass
		elif img['src'] == "http://a.deviantart.net/avatars/default.gif":
			pass
		try:
			count = count + 1
			image_url = img['src']
			image_name = str.split(image_url, '/')
			urllib.request.urlretrieve(image_url, path + "/" + image_name[-1])
		except:
			pass
	c = c + 25
