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
filename = curdir + '/log/beginLog.txt'  
f = open(filename,'w')
f.write("日志文件创建成功：       " + getTime())
f.flush()
print "create logfile success"


#创建截图存放的文件夹
if not os.path.exists(curdir + '\screenShot\unlogin'):
    os.mkdir(curdir + '\screenShot\unlogin')
print "screenShot folder created"


#创建截图的解释文件
filename2 = curdir + '/screenShot/unlogin/readme.txt'
fi = open(filename2,'w')
print "create screenshot details file success"


#启动秒拍apk
print "start miaiopai app"
package = 'com.yixia.videoeditor'
activity = 'com.yixia.videoeditor.ui.login.SplashActivity'
runComponent = package + '/' + activity
device.startActivity(component=runComponent)
f.write("启动秒拍：       " + getTime() + "\n")
f.flush()
MonkeyRunner.sleep(10.0)



#一下是正式的操作代码
print "start oparation ..."
print "**********************************************"
print "excute case sets: 'unlogin status'"
f.write("**********************************************\n")
f.write("                 用例执行                       \n")
f.write("**********************************************\n\n")
f.flush()

#------------------------将转换后的自动化脚本复制到以下区域即可--------------------------------


device.touch(389,1229,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
device.touch(474,725,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
device.touch(274,229,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
device.type("13146201117")
MonkeyRunner.sleep(2.0)
device.touch(337,317,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
device.type("123456")


MonkeyRunner.sleep(2.0)
device.touch(420,448,"DOWN_AND_UP")



#------------------------将转换后的自动化脚本复制到以上区域即可--------------------------------


print "end..."
f.close()
fi.close
