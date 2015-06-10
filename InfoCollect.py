#!/usr/bin/python
#coding:utf-8
import commands
from FileUtil import FileUtil

class InfoCollect():
    def __init__(self, filePath, siteName):
	self.filePath = filePath
	self.siteName = siteName
	self.fileUtil = FileUtil()

    def getInfo(self, strCommand):
	if strCommand == 'whois':
	    command = 'whois ' + self.siteName
	elif strCommand == 'whatweb':
	    command = 'whatweb ' + self.siteName
	elif strCommand == 'dig':
	    command = 'dig @114.114.114.114 ' + self.siteName + ' any'
	(status, results) = commands.getstatusoutput(command)
	self.fileUtil.writeFile("Status:" + str(status) + "\n\n" + results, self.filePath + strCommand + '.txt', 'w')
	print strCommand + self.siteName + '收集完毕！'
    
