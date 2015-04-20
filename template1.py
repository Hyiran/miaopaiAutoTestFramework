#coding=utf-8
import sys
import time
import os

print
print
print "###############################################"
print
print "          start run automatic script           "
print
print "###############################################"
print "----start----"

curdir = sys.argv[0]
index = curdir.rfind("\\")
curdir = curdir[:index]

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

#创建运行日志文件
filename = curdir + '/log/beginLog.txt'  
f = open(filename,'w')
f.write("日志文件创建成功：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
print "create logfile success"

#创建截图存放的文件夹
if not os.path.exists(curdir + '\screenShot\unlogin'):
    os.mkdir(curdir + '\screenShot\unlogin')
print "screenShot folder created"

#连接设备
print "connecting device..."
device = MonkeyRunner.waitForConnection()
f.write("设备连接成功：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()

#启动秒拍apk
print "start miaiopai app"
package = 'com.yixia.videoeditor'
activity = 'com.yixia.videoeditor.ui.login.SplashActivity'
runComponent = package + '/' + activity
device.startActivity(component=runComponent)
f.write("启动秒拍：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n\n")
f.flush()
MonkeyRunner.sleep(5.0)


#一下是正式的操作代码
print "start oparation ..."
print "**********************************************"
print "excute case sets: 'unlogin status'"
f.write("**********************************************\n")
f.write("         未登录情况用例执行                       \n")
f.write("**********************************************\n\n")
f.flush()

#------------------------将转换后的自动化脚本复制到以下区域即可--------------------------------






#将转换后的自动化脚本复制到此区域即可


##device.touch(184,1229,"DOWN_AND_UP")
##MonkeyRunner.sleep(3.0)
##device.touch(387,1226,"DOWN_AND_UP")
##MonkeyRunner.sleep(3.0)
##device.touch(558,376,"DOWN_AND_UP")
##MonkeyRunner.sleep(3.0)
##device.touch(535,1234,"DOWN_AND_UP")
##MonkeyRunner.sleep(3.0)
##device.touch(654,1224,"DOWN_AND_UP")
##MonkeyRunner.sleep(3.0)
##device.touch(54,96,"DOWN_AND_UP")



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
