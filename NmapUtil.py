#!/usr/bin/python
#coding:utf-8
import os

class NmapUtil:
    """
    Nmap工具类
    ip : 被扫描主机IP地址
    portList : 常见端口列表
    nmapResultFile : Nmap扫描结果文件
    """

    #创建NMAP线程
    def thread_nmap(self, ip, portList, nmapResultFile):
	command  = 'nmap -v -T5 -P0 -sT -p ' + portList + ' ' + ip  + '  --open | grep "Discovered" >> ' + nmapResultFile
	os.popen(command)

