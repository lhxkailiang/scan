#!/usr/bin/python
#coding:utf-8
import os

class PathUtil:
    """
    文件路径工具类
    dnsResultFilePath  : dns结果存放路径
    nmapResultFilePath : nmap结果存放路径
    infoResultFilePath : whois whatweb dig信息存放路径
    """
    #创建结果存放路径及文件
    def createFilePath(self, dnsResultFilePath, nmapResultFilePath, infoResultFilePath):
	#dns结果文件
        if os.path.exists(dnsResultFilePath):
	   pass
	else:
	    os.makedirs(dnsResultFilePath)
        #nmap结果文件夹
	if os.path.exists(nmapResultFilePath):
	    pass
        else:
	    os.makedirs(nmapResultFilePath)
	#info信息文件夹
	if os.path.exists(infoResultFilePath):
	    pass
	else:
	    os.makedirs(infoResultFilePath)
	print "domain结果文件夹:" + dnsResultFilePath
	print "Nmap结果文件夹:" + nmapResultFilePath
	print "Whois Whatweb dig信息文件夹:" + infoResultFilePath

