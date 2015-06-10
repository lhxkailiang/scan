#!/usr/bin/python
#coding:utf-8
import time
import sys
from optparse import OptionParser
from FileUtil import FileUtil
from PathUtil import PathUtil
from QueueUtil import QueueUtil
from InfoCollect import InfoCollect

#获取dnf密码字典中的域名的IP地址并分类
def getDNSIP(domainNameList, dnsResultFilePath, currentTime):
    privateIPFile = open(dnsResultFilePath + currentTime + '_Private', 'w')
    publicIPFile = open(dnsResultFilePath + currentTime + '_Public', 'w')
    allIPFile = open(dnsResultFilePath + currentTime + '_All', 'w')
    errorInfoFile = open(dnsResultFilePath + currentTime + '_Error', 'w')
    print "正在解析DNS字典中域名的IP地址,请耐心等待..."
    #IP段列表
    ipPublicList = []
    ipPrivateList = []
    for i in domainNameList:
	try:
	    ip = socket.gethostbyname(i)
	    allIPFile.write(ip + "\t" + i + "\n")
	    ipSplitList = ip.split('.')
	    ip0 = int(ipSplitList[0])
	    ip1 = int(ipSplitList[1])
	    ip2 = int(ipSplitList[2])
	    ipStage = str(ip0) + '.' + str(ip1) + '.' + str(ip2)
	    #区分私有IP地址
	    if ip0 == 10 or ip0 == 172 and ip1 >= 16 and ip1 <= 31 or ip0 == 192 and ip1 == 168:
		if ipStage not in ipPrivateList:
		    ipPrivateList.append(ipStage)
                    privateIPFile.write(ipStage + "\n")
	    else:
		if ipStage not in ipPublicList:
		    ipPublicList.append(ipStage)
                    publicIPFile.write(ipStage + "\n")
	except Exception,e:
	    allIPFile.write(i + "\t" + str(e) + "\n")
	    errorInfoFile.write(i + "\t" + str(e) + "\n")
    privateIPFile.close()
    publicIPFile.close()
    allIPFile.close()
    errorInfoFile.close()
    print "DNS解析IP成功,IP地址段已成功分类,请查看domain结果文件夹! " + dnsResultFilePath
    return ipPublicList

def getPortList(portFilePath):
    portFile = open(portFilePath, 'r')
    portList = ''
    for eachLine in portFile:
	portList = eachLine.strip()
    portFile.close()
    print "常用端口读取成功!"
    return portList


#主程序入口
if __name__=="__main__":
    #结果文件存放主目录
    resultFilePath = '/usr/scanResult/'
    #域名字典存放目录
    domainListDic = '/python_tools/scan/resource/dnsDic.txt'
    #常见端口列表文件
    portFilePath = '/python_tools/scan/resource/portList'
    #队列数
    queueNumber = 10

    #查询的主域名
    parser = OptionParser()
    parser.add_option("-d", "--domain", action="store", dest="domain", default=False,type="string",help="test domain")
    (options, args) = parser.parse_args()
    if(options.domain):
	domainName = options.domain
    else:
	sys.exit(1)
    
    print "主域名：" + domainName
    siteName = domainName.split('.')[0]
    #获取当前时间
    currentTime = time.strftime('%Y%m%d_%H%M%S',time.localtime(int(time.time())))
    print "当前时间:" + currentTime
    #创建結果文件夾及文件
    dnsResultFilePath = resultFilePath + siteName + '/domain/'
    nmapResultFilePath = resultFilePath + siteName + '/nmap/'
    infoResultFilePath = resultFilePath + siteName + '/info/'
    nmapResultFile = nmapResultFilePath + currentTime + '.txt'
    #创建扫描结果存放路径
    pathUtil = PathUtil()
    pathUtil.createFilePath(dnsResultFilePath, nmapResultFilePath, infoResultFilePath)
    #收集信息
    infoCollect = InfoCollect(infoResultFilePath, domainName)
    infoCollect.getInfo('whois')
    infoCollect.getInfo('whatweb')
    infoCollect.getInfo('dig')

    #读取dns字典
    fileUtil = FileUtil()
    domainList = fileUtil.getdomainNameList(domainName, domainListDic)
    #获取dnf密码字典中的域名的IP地址并分类
    finalIPList = getDNSIP(domainList, dnsResultFilePath, currentTime)
    #获取端口列表
    portList = getPortList(portFilePath) 
    #创建扫描队列
    queueUtil = QueueUtil()
    queueUtil.createQueue(finalIPList, portList, nmapResultFile, queueNumber)
