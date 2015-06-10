#!/usr/bin/python
#coding:utf-8
import Queue
import threading
from NmapUtil import NmapUtil
from IPUtil import IPUtil

class QueueUtil:
    """
    队列工具类
    IPList : IP地址列表
    portList : 常见端口列表
    nmapResultFile : Nmap扫描结果文件
    queueNumber : 队列数目 
    """

    #创建扫描队列
    def createQueue(self, IPList, portList, nmapResultFile, queueNumber):
	ipUtil = IPUtil()
	nmapUtil = NmapUtil()
	print "队列创建中..."
        queue_list = Queue.Queue()
	for i in IPList:
	    iplist = ipUtil.createIPList(i.strip(), 24)
            for x in iplist:
		#创建线程
		t = threading.Thread(target=nmapUtil.thread_nmap,args=(x, portList, nmapResultFile))
		queue_list.put(t)
	print "对列总数为:" + str(queue_list.qsize())
    
	#队列数量
	print "正在对域名中IP段的主机进行扫描,请耐心等待..."
	while not queue_list.empty():
	    print "当前剩余任务数：" + str(queue_list.qsize())
	    if queue_list.qsize() < queueNumber:
		queueNumber = queue_list.qsize()

	    threads = []
	    for t in range(queueNumber):
		nmapThread = queue_list.get()
		threads.append(nmapThread)

	    for x in threads:
		x.start()
	    for y in threads:
		y.join()
	print "扫描已完成，请查看扫描结果！结果文件位于：" + nmapResultFile 
