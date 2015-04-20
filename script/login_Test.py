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
filename = curdir + '/log/login_TestLog.txt'  
f = open(filename,'w')
f.write("日志文件创建成功：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
print "create logfile success"

#创建截图存放的文件夹
if not os.path.exists(curdir + '\screenShot\login_Test'):
    os.mkdir(curdir + '\screenShot\login_Test')
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
##我的页面登录测试；设置页面登录测试；点击拍摄按钮登录测试
##测试步骤：
##1、点击我
##2、点击立即登录
##3、点击手机号
##4、输入手机号码“18611513354”
##5、点击密码框
##6、输入密码
##7、点击登录按钮
##8、点击设置按钮
##9、点击退出登录
##10、点击确定按钮
##11、点击设置页面的立即登录
##12、点击手机号
##13、输入手机号码“18611513354”
##14、点击密码框
##15、输入密码
##16、点击登录
##17、点击退出登录
##18、点击取消按钮
##19、点击退出登录
##20、点击确定按钮
##21、点击返回退出设置页面
##22、点击首页
##23、点击拍摄按钮
##24、点击手机号
##25、输入手机号码“18611513354”
##26、点击密码框
##27、输入密码
##28、点击登录按钮


##1、点击我
device.touch(652,1224,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##2、点击立即登录
device.touch(366,698,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##3、点击手机号
device.touch(463,736,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##4、输入手机号码“18611513354”
device.type("18611513354")
MonkeyRunner.sleep(2.0)
##5、点击密码框
device.touch(207,314,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##6、输入密码
device.type("123456")
MonkeyRunner.sleep(2.0)
##7、点击登录按钮
device.touch(371,434,"DOWN_AND_UP")
MonkeyRunner.sleep(5.0)
##8、点击设置按钮
device.touch(51,96,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##9、点击退出登录
device.touch(382,1034,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##10、点击确定按钮
device.touch(528,744,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##11、点击设置页面的立即登录
device.touch(389,949,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##12、点击手机号
device.touch(445,733,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##13、输入手机号码“18611513354”
device.type("18611513354")
MonkeyRunner.sleep(2.0)
##14、点击密码框
device.touch(270,309,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##15、输入密码
device.type("123456")
MonkeyRunner.sleep(2.0)
##16、点击登录
device.touch(351,432,"DOWN_AND_UP")
MonkeyRunner.sleep(5.0)
##17、点击退出登录
device.touch(373,1040,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##18、点击取消按钮
device.touch(234,746,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##19、点击退出登录
device.touch(389,1037,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##20、点击确定按钮
device.touch(531,738,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##21、点击返回退出设置页面
device.touch(36,93,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##22、点击首页
device.touch(63,1226,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##23、点击拍摄按钮
device.touch(357,1216,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##24、点击手机号
device.touch(474,768,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##25、输入手机号码“18611513354”
device.type("18611513354")
MonkeyRunner.sleep(2.0)
##26、点击密码框
device.touch(333,306,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##27、输入密码
device.type("123456")
MonkeyRunner.sleep(2.0)
##28、点击登录按钮
device.touch(360,432,"DOWN_AND_UP")

#------------------------将转换后的自动化脚本复制到以上区域即可--------------------------------


print "end..."
f.close()
