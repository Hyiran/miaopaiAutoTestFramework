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
filename = curdir + '/log/searchTestLog.txt'  
f = open(filename,'w')
f.write("日志文件创建成功：       " + getTime())
f.flush()
print "create logfile success"


#创建截图存放的文件夹
if not os.path.exists(curdir + '\\screenShot\\searchTest'):
    os.mkdir(curdir + '\\screenShot\\searchTest')
print "screenShot folder created"


#创建截图的解释文件
filename2 = curdir + '/screenShot/searchTest/readme.txt'
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
print "excute case sets: 'searchTest status'"
f.write("**********************************************\n")
f.write("                 用例执行                       \n")
f.write("**********************************************\n\n")
f.flush()

#------------------------将转换后的自动化脚本复制到以下区域即可--------------------------------
##1、点击首页左上角的搜索按钮
##2、点击取消退出该页面
##3、再次点击首页左上角的搜索按钮
##4、输入yiixia66点击
##5、点击收索
##6、点击用户列表
##7、点击用户列表的第一个，进入该用户的主页
##8、点击返回按钮，退出用户户主页
##9、再次点击返回按钮，返回到搜索页面
##10、点击取消按钮，返回到首页

##1、点击首页左上角的搜索按钮
##2、点击取消退出该页面
device.touch(675,90,"DOWN_AND_UP")
writeToLog(f,"点击首页左上角的搜索按钮")
MonkeyRunner.sleep(2.0)
device.touch(47,96,"DOWN_AND_UP")
writeToLog(f,"点击取消退出该页面")
MonkeyRunner.sleep(2.0)
##3、再次点击首页左上角的搜索按钮
device.touch(668,90,"DOWN_AND_UP")
writeToLog(f,"再次点击首页左上角的搜索按钮")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"searchTest",1)
writeToDetails(fi,"1、搜索页面截图")
##4、输入yiixia66点击
##5、点击收索
device.type("yiixia66")
writeToLog(f,"输入yiixia66点击")
MonkeyRunner.sleep(2.0)
device.touch(677,96,"DOWN_AND_UP")
writeToLog(f,"点击收索")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"searchTest",2)
writeToDetails(fi,"2、搜索结果截图")
##6、点击用户列表
device.touch(54,282,"DOWN_AND_UP")
writeToLog(f,"点击用户列表")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"searchTest",3)
writeToDetails(fi,"3、搜索用户列表截图")
##7、点击用户列表的第一个，进入该用户的主页
device.touch(166,189,"DOWN_AND_UP")
writeToLog(f,"点击用户列表的第一个，进入该用户的主页")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"searchTest",4)
writeToDetails(fi,"4、用户主页截图")
##8、点击返回按钮，退出用户户主页
##9、再次点击返回按钮，返回到搜索页面
##10、点击取消按钮，返回到首页
device.touch(45,98,"DOWN_AND_UP")
writeToLog(f,"点击返回按钮，退出用户户主页")
MonkeyRunner.sleep(2.0)
device.touch(38,96,"DOWN_AND_UP")
writeToLog(f,"再次点击返回按钮，返回到搜索页面")
MonkeyRunner.sleep(2.0)
device.touch(56,101,"DOWN_AND_UP")
writeToLog(f,"点击取消按钮，返回到首页")
MonkeyRunner.sleep(2.0)


#------------------------将转换后的自动化脚本复制到以上区域即可--------------------------------


print "end..."
f.close()
fi.close
