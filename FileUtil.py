#!/usr/bin/python
#coding:utf-8

class FileUtil:
    """
    文件工具类
    domainName : 主域名
    domainListDic : 域名字典文件路径
    """

    #读取域名字典文件并返回域名列表
    def getdomainNameList(self, domainName, domainListDic):
	fileObject = open(domainListDic, 'r')
        domainNameList = []
	for eachLine in fileObject:
	    domainNameList.append(eachLine.strip()+ '.' +domainName)
	print "DNS字典列表读取成功!"
	return domainNameList

    def readFile(self, filePath):
	pass

    def writeFile(self, content, filePath, writeMode):
	f = open(filePath, writeMode)
	f.write(content + "\n")
	f.close()
	

