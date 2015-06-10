#!/usr/bin/python
#coding:utf-8
import urllib2

class WebSpider:
    def searchBacker(self, ip, port):
	url = 'http://' + ip + ':' + port
	response = urllib2.urlopen(url)
	htmlCode = response.read()
	if 'username' in htmlCode:
	    print 'username'



if __name__ == '__main__':
    webSpider = WebSpider()
    webSpider.searchBacker('58.83.206.9', '8888')

