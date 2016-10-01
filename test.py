#codinge=utf-8
import re
import urllib
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
def getImg(html):
	imgre = re.compile('<div class="price">.*?</span>(.*?)<span .*?>.*?</div>',re.S)
	imglist = re.findall(imgre,html)
	return imglist

s = getHtml("http://lvhe365.com/")
print getImg(s)
