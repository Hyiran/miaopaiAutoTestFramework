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
filename = curdir + '/log/commentTestLog.txt'  
f = open(filename,'w')
f.write("日志文件创建成功：       " + getTime())
f.flush()
print "create logfile success"


#创建截图存放的文件夹
if not os.path.exists(curdir + '\\screenShot\\commentTest'):
    os.mkdir(curdir + '\\screenShot\\commentTest')
print "screenShot folder created"


#创建截图的解释文件
filename2 = curdir + '/screenShot/commentTest/readme.txt'
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
print "excute case sets: 'commentTest status'"
f.write("**********************************************\n")
f.write("                 用例执行                       \n")
f.write("**********************************************\n\n")
f.flush()

#------------------------将转换后的自动化脚本复制到以下区域即可--------------------------------
##1、点击进入详情页面
##2、不输入任何内容，点击评论的发送按钮
##3、点击评论输入框
##4、输入hello
##5、点击发送
##6、向上滚动页面
##7、点击评论输入框
##8、再次输入hello
##9、点击发送
##10、点击返回按钮，返回到首页

##1、点击进入详情页面
##2、不输入任何内容，点击评论的发送按钮
device.touch(200,437,"DOWN_AND_UP")
writeToLog(f,"点击进入详情页面")
MonkeyRunner.sleep(3.0)
device.touch(684,1229,"DOWN_AND_UP")
writeToLog(f,"不输入任何内容，点击评论的发送按钮")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"commentTest",1)
writeToDetails(fi,"1、评论不输入任何内容，点击发送弹出toast提示截图")
##3、点击评论输入框
##4、输入hello
##5、点击发送
##6、向上滚动页面
device.touch(303,1232,"DOWN_AND_UP")
writeToLog(f,"点击评论输入框")
MonkeyRunner.sleep(2.0)
device.type("hello")
writeToLog(f,"输入hello")
MonkeyRunner.sleep(2.0)
device.touch(686,784,"DOWN_AND_UP")
writeToLog(f,"点击发送")
MonkeyRunner.sleep(2.0)
device.drag((288,1024),(288,204),1.0,10)
writeToLog(f,"向上滚动页面")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"commentTest",2)
writeToDetails(fi,"2、评论发送成功截图")
##7、点击评论输入框
##8、再次输入hello
##9、点击发送
device.touch(427,1232,"DOWN_AND_UP")
writeToLog(f,"点击评论输入框")
MonkeyRunner.sleep(2.0)
device.type("hello")
writeToLog(f,"再次输入hello")
MonkeyRunner.sleep(2.0)
device.touch(679,792,"DOWN_AND_UP")
writeToLog(f,"点击发送")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"commentTest",3)
writeToDetails(fi,"3、评论发送失败截图")
##10、点击返回按钮，返回到首页
device.touch(38,90,"DOWN_AND_UP")
writeToLog(f,"点击返回按钮，返回到首页")
MonkeyRunner.sleep(2.0)


#------------------------将转换后的自动化脚本复制到以上区域即可--------------------------------


print "end..."
f.close()
fi.close
