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

print
print
print "###############################################"
print
print "          start run automatic script           "
print
print "###############################################"
print "----start----"



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



#连接设备
print "connecting device..."
device = MonkeyRunner.waitForConnection()
f.write("设备连接成功：       " + getTime())
f.flush()


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
f.write("         未登录情况用例执行                       \n")
f.write("**********************************************\n\n")
f.flush()

##【未登录情况下测试】测试步骤：
##1、点击进入详情页开始播放
##2、点击视频区域停止播放
##3、点击加关注按钮
##4、点击关闭登录对话框
##5、向上滑动
##6、双击喜欢                ----   未执行
##7、点击关闭登录对话框        ----   未执行
##8、点赞按钮                ----   未执行
##9、点击关闭登录对话框        ----   未执行
##10、点击分享               ----   未执行
##11、点击关闭登录对话框       ----   未执行
##12、点击发送按钮
##13、点击关闭登录对话框
##14、点击返回退出详情页面
##15、点击拍摄按钮
##16、点击关闭登录对话框
##17、点击好友
##18、点击立即登录
##19、点击关闭登录对话框
##20、点击我
##21、点击立即登录
##22、点击关闭登录对话框
##23、点击设置
##24、点击立即登录
##25、点击关闭登录对话框
##26、点击返回退出设置页面
##27、点击首页

#-----------------------将转换后的代码复制到以下位置------------------------------
#点击进入详情页并开始播放视频
device.touch(182,314,"DOWN_AND_UP")
f.write("点击进入详情页并开始播放视频：       " + getTime())
MonkeyRunner.sleep(10.0)
getPic(device,curdir,"unlogin",1)
#点击停止播放
device.touch(389,650,"DOWN_AND_UP")
f.write("点击停止播放：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)

#点击加关注按钮
device.touch(641,205,"DOWN_AND_UP")
f.write("点击加关注按钮：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"unlogin",2)

#点击关闭登录对话框
device.touch(555,376,"DOWN_AND_UP")
f.write("点击关闭登录对话框：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#向上滑动
device.drag((288,1024),(288,724),1.0,10)
f.write("向上滑动：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#双击喜欢
device.touch(400,418,"DOWN_AND_UP")
device.touch(400,418,"DOWN_AND_UP")
f.write("双击喜欢：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#点击关闭登录对话框
device.touch(555,370,"DOWN_AND_UP")
f.write("点击关闭登录对话框：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)

#-------------------------------------------------------------------------------------------------
###点击喜欢按钮
##device.touch(461,1034,"DOWN_AND_UP")
##f.write("点击喜欢按钮：       " + getTime())
##f.flush()
##MonkeyRunner.sleep(2.0)
###点击关闭登录对话框
##device.touch(560,373,"DOWN_AND_UP")
##f.write("点击关闭登录对话框：       " + getTime())
##f.flush()
##MonkeyRunner.sleep(2.0)
###点击分享
##device.touch(621,1024,"DOWN_AND_UP")
##f.write("点击分享：       " + getTime())
##f.flush()
##MonkeyRunner.sleep(2.0)
###点击关闭登录对话框
##device.touch(555,376,"DOWN_AND_UP")
##f.write("点击关闭登录对话框：       " + getTime())
##f.flush()
##MonkeyRunner.sleep(2.0)
#-------------------------------------------------------------------------------------------------
#点击发送按钮
device.touch(679,1224,"DOWN_AND_UP")
f.write("点击发送按钮：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#点击关闭登录对话框
device.touch(560,365,"DOWN_AND_UP")
f.write("点击关闭登录对话框：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#点击返回退出详情页面
device.touch(38,90,"DOWN_AND_UP")
f.write("点击返回退出详情页面：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#点击拍摄按钮
device.touch(366,1221,"DOWN_AND_UP")
f.write("点击拍摄按钮：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"unlogin",3)
#点击关闭登录对话框
device.touch(558,373,"DOWN_AND_UP")
f.write("点击关闭登录对话框：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#点击好友
device.touch(531,1232,"DOWN_AND_UP")
f.write("点击好友：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#点击立即登录
device.touch(393,706,"DOWN_AND_UP")
getPic(device,curdir,"unlogin",4)
f.write("点击立即登录：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#点击关闭登录对话框
device.touch(560,376,"DOWN_AND_UP")
f.write("点击关闭登录对话框：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#点击我
device.touch(652,1229,"DOWN_AND_UP")
f.write("点击我：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#点击立即登录
device.touch(364,704,"DOWN_AND_UP")
f.write("点击立即登录：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"unlogin",5)
#点击关闭登录对话框
device.touch(560,373,"DOWN_AND_UP")
f.write("点击关闭登录对话框：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#点击设置
device.touch(58,104,"DOWN_AND_UP")
f.write("点击设置：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#点击立即登录
device.touch(398,952,"DOWN_AND_UP")
f.write("点击立即登录：       " + getTime())
f.flush()
getPic(device,curdir,"unlogin",6)
#点击关闭登录对话框
device.touch(555,370,"DOWN_AND_UP")
f.write("点击关闭登录对话框：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#点击返回退出设置页面
device.touch(45,93,"DOWN_AND_UP")
f.write("点击返回退出设置页面       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)
#点击首页
device.touch(63,1221,"DOWN_AND_UP")
f.write("点击首页：       " + getTime())
f.flush()
MonkeyRunner.sleep(2.0)

#-----------------------将转换后的代码复制到以上位置------------------------------


print "end..."
f.close()


