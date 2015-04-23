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
filename = curdir + '/log/mobileLoginLog.txt'  
f = open(filename,'w')
f.write("日志文件创建成功：       " + getTime())
f.flush()
print "create logfile success"


#创建截图存放的文件夹
if not os.path.exists(curdir + '\\screenShot\\mobileLogin'):
    os.mkdir(curdir + '\\screenShot\\mobileLogin')
print "screenShot folder created"


#创建截图的解释文件
filename2 = curdir + '/screenShot/mobileLogin/readme.txt'
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
##1、点击拍摄按钮
##2、点击登陆界面的手机号
##3、点击手机号登陆页面的手机号输入框
##4、输入手机号18600989561
##5、点击密码输入框
##6、输入小于6为的密码
##7、点击登陆
##8、输入错误的密码
##9、点击登录
##10、输入正确的密码
##11、点击登录

device.touch(364,1226,"DOWN_AND_UP")
writeToLog(f,"点击拍摄按钮")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"mobileLogin",1)
writeToDetails(fi,"1、点击拍摄按钮弹出登陆界面截图")

device.touch(479,738,"DOWN_AND_UP")
writeToLog(f,"点击登陆界面的手机号")
MonkeyRunner.sleep(2.0)

device.touch(366,218,"DOWN_AND_UP")
writeToLog(f,"点击手机号登陆页面的手机号输入框")
MonkeyRunner.sleep(2.0)

device.type("18600989561")
writeToLog(f,"输入手机号18600989561")
MonkeyRunner.sleep(2.0)

device.touch(308,320,"DOWN_AND_UP")
writeToLog(f,"击密码输入框")
MonkeyRunner.sleep(2.0)

device.type("12")
writeToLog(f,"输入小于6为的密码")
MonkeyRunner.sleep(2.0)

device.touch(387,434,"DOWN_AND_UP")
writeToLog(f,"点击登录")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"mobileLogin",2)
writeToDetails(fi,"2、输入小于六位的密码截图")
device.press("KEYCODE_DEL","DOWN_AND_UP")
MonkeyRunner.sleep(0.3)
device.press("KEYCODE_DEL","DOWN_AND_UP")
MonkeyRunner.sleep(1.0)

device.type("1234567")
writeToLog(f,"输入错误的密码")
MonkeyRunner.sleep(2.0)
device.touch(357,445,"DOWN_AND_UP")
writeToLog(f,"点击登录")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"mobileLogin",3)
writeToDetails(fi,"3、输入错误的密码截图")
device.press("KEYCODE_DEL","DOWN_AND_UP")
MonkeyRunner.sleep(0.3)
device.press("KEYCODE_DEL","DOWN_AND_UP")
MonkeyRunner.sleep(0.3)
device.press("KEYCODE_DEL","DOWN_AND_UP")
MonkeyRunner.sleep(0.3)
device.press("KEYCODE_DEL","DOWN_AND_UP")
MonkeyRunner.sleep(0.3)
device.press("KEYCODE_DEL","DOWN_AND_UP")
MonkeyRunner.sleep(0.3)
device.press("KEYCODE_DEL","DOWN_AND_UP")
MonkeyRunner.sleep(0.3)
device.press("KEYCODE_DEL","DOWN_AND_UP")
MonkeyRunner.sleep(1.0)

device.type("123456")
writeToLog(f,"输入正确的密码")
MonkeyRunner.sleep(2.0)

device.touch(409,450,"DOWN_AND_UP")
writeToLog(f,"点击登录")
MonkeyRunner.sleep(6.0)
getPic(device,curdir,"mobileLogin",4)
writeToDetails(fi,"4、首页截图")




#------------------------将转换后的自动化脚本复制到以上区域即可--------------------------------


print "end..."
f.close()
fi.close
