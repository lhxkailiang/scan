#!/usr/bin/python
#coding:utf-8

class IPUtil:
    """
    IP Util
    ip : ip地址
    scope : 16B段 24C段
    """

    #生成IP地址范围
    def createIPList(self, ip, scope):
	ipList = []
	lists = ip.split('.')
	if scope == 24:
	    for x in range(1,256):
		ipList.append(lists[0] + '.' + lists[1] + '.' + lists[2] + '.' + str(x))
	elif scope == 16:
	    for x in range(1,256):
		for y in range(1,256):
		    ipList.append(lists[0] + '.' + lists[1] + '.' + str(x) + '.' + str(y))
        return ipList
