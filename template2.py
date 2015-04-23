#coding=utf-8
import sys
import time
import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


#获取时间，并返回具体时间的函数
def getTime():
    return "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n"

#截图，并保存图片的函数
def getPic(device,curdir,path,num):
    result = device.takeSnapshot()
    result.writeToFile(curdir + '/screenShot/' + path + '/' + str(num) + '.png','png')
    print "end screenshot: " + str(num) + ".png"

#写入相应的日志
def writeToLog(f,string):
    f.write(string + getTime())
    f.flush()

def writeToDetails(fi,details):
    fi.write(details + "\n")
    fi.flush()

#连接设备
print "connecting device..."
device = MonkeyRunner.waitForConnection()

print
print
print "###############################################"
print
print "          start run automatic script           "
print
print "###############################################"
print
#显示手机型号
print str(device.getProperty('build.model'))
#获取手机的width,height
print 'width'+ ':'+ str(device.getProperty('display.width'))
print 'height'+ ':'+ str(device.getProperty('display.height'))
print
print "###############################################"
print "-----start-----"


#获取当前目录
curdir = sys.argv[0]
index = curdir.rfind("\\")
curdir = curdir[:index]


#创建运行日志文件
filename = curdir + '/log/template2Log.txt'  
f = open(filename,'w')
f.write("日志文件创建成功：       " + getTime())
f.flush()
print "create logfile success"


#创建截图存放的文件夹
if not os.path.exists(curdir + '\\screenShot\\template2'):
    os.mkdir(curdir + '\\screenShot\\template2')
print "screenShot folder created"


#创建截图的解释文件
filename2 = curdir + '/screenShot/template2/readme.txt'
fi = open(filename2,'w')
print "create screenshot details file success"


#安装apk
device.installPackage(curdir + '\\apk\\miaopai510.apk')
print "install successfully !"
print

#启动秒拍apk
package = 'com.yixia.videoeditor'
activity = 'com.yixia.videoeditor.ui.login.SplashActivity'
runComponent = package + '/' + activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(10.0)



#------------------------将转换后的自动化脚本复制到以下区域即可--------------------------------



result = device.takeSnapshot()
getPic(device,curdir,"template2",1)
print "end screenshot: yingdaotu.png"
MonkeyRunner.sleep(1.0)

device.drag((384,341),(76,341),1.0,10)
MonkeyRunner.sleep(5.0)





#------------------------将转换后的自动化脚本复制到以上区域即可--------------------------------

print "uninstalling ......."
device.removePackage('com.yixia.videoeditor')
print "uninstalled"
print "end..."
f.close()
fi.close

