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
filename = curdir + '/log/seting_page_testLog.txt'  
f = open(filename,'w')
f.write("日志文件创建成功：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
print "create logfile success"

#创建截图存放的文件夹
if not os.path.exists(curdir + '\screenShot\setting_page_Test'):
    os.mkdir(curdir + '\screenShot\setting_page_Test')
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
f.write("         设置页面用例执行                       \n")
f.write("**********************************************\n\n")
f.flush()

#------------------------将转换后的自动化脚本复制到以下区域即可--------------------------------
#执行的步骤
##--------------------------------------
##设置页面测试：
##1、点击底导上的我
##2、点击设置按钮
##3、关闭wifi下自动播放
##4、打开3G拍摄使用较低画质
##5、打开静音
##6、打开wifi下自动播放
##7、关闭3G拍摄使用较低画质
##8、关闭静音
##9、点击新消息提醒，进入新消息提醒页面
##10、关闭新粉丝
##11、关闭评论
##12、关闭喜欢
##13、打开新粉丝
##14、打开评论
##15、打开喜欢
##16、点击返回按钮，退出新消息提醒页面
##17、点击意见反馈
##18、不输入任何内容点击发送
##
##19、点击文本区
##20、输入“test”
##21、点击发送
##22、点击清空缓存
##23、点击否
##24、点击清空缓存
##25、点击是
##26、点击版本检测

##1、点击底导上的我
device.touch(657,1232,"DOWN_AND_UP")
f.write("点击底导上的我：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##2、点击设置按钮
device.touch(56,93,"DOWN_AND_UP")
f.write("点击设置按钮：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(3.0)
##3、关闭wifi下自动播放
device.touch(652,237,"DOWN_AND_UP")
f.write("关闭wifi下自动播放：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##4、打开3G拍摄使用较低画质
device.touch(639,328,"DOWN_AND_UP")
f.write("打开3G拍摄使用较低画质：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##5、打开静音
device.touch(636,416,"DOWN_AND_UP")
f.write("打开静音：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##6、打开wifi下自动播放
device.touch(639,221,"DOWN_AND_UP")
f.write("打开wifi下自动播放：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##7、关闭3G拍摄使用较低画质
device.touch(650,341,"DOWN_AND_UP")
f.write("关闭3G拍摄使用较低画质：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##8、关闭静音
device.touch(661,434,"DOWN_AND_UP")
f.write("关闭静音：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##9、点击新消息提醒，进入新消息提醒页面
device.touch(247,517,"DOWN_AND_UP")
f.write("点击新消息提醒，进入新消息提醒页面：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##10、关闭新粉丝
device.touch(672,256,"DOWN_AND_UP")
f.write("关闭新粉丝：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##11、关闭评论
device.touch(670,346,"DOWN_AND_UP")
f.write("关闭评论：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##12、关闭喜欢
device.touch(668,458,"DOWN_AND_UP")
f.write("关闭喜欢：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##13、打开新粉丝
device.touch(623,250,"DOWN_AND_UP")
f.write("打开新粉丝：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##14、打开评论
device.touch(632,349,"DOWN_AND_UP")
f.write("打开评论：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##15、打开喜欢
device.touch(636,464,"DOWN_AND_UP")
f.write("打开喜欢：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##16、点击返回按钮，退出新消息提醒页面
device.touch(47,101,"DOWN_AND_UP")
f.write("点击返回按钮，退出新消息提醒页面：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##17、点击意见反馈
device.touch(360,658,"DOWN_AND_UP")
f.write("点击意见反馈：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##18、不输入任何内容点击发送
device.touch(654,101,"DOWN_AND_UP")
f.write("不输入任何内容点击发送：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)

##19、点击文本区
device.touch(74,202,"DOWN_AND_UP")
f.write("点击文本区：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##20、输入“test”
device.type("test")
f.write("输入\“test\”：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##21、点击发送
device.touch(663,101,"DOWN_AND_UP")
f.write("点击发送：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##22、点击清空缓存
device.touch(357,909,"DOWN_AND_UP")
f.write("点击清空缓存：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##23、点击否
device.touch(234,746,"DOWN_AND_UP")
f.write("点击否：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##24、点击清空缓存
device.touch(353,906,"DOWN_AND_UP")
f.write("点击清空缓存：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##24、点击是
device.touch(535,746,"DOWN_AND_UP")
f.write("点击是：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)
##26、点击版本检测
device.touch(225,760,"DOWN_AND_UP")
f.write("点击版本检测：       " + "[" + time.strftime('%Y-%m-%d') + "   " + time.strftime('%H:%M:%S') + "]\n")
f.flush()
MonkeyRunner.sleep(2.0)


#------------------------将转换后的自动化脚本复制到以上区域即可--------------------------------


print "end..."
f.close()
