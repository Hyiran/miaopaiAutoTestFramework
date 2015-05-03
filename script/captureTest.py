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
filename = curdir + '/log/captureTestLog.txt'  
f = open(filename,'w')
f.write("日志文件创建成功：       " + getTime())
f.flush()
print "create logfile success"


#创建截图存放的文件夹
if not os.path.exists(curdir + '\\screenShot\\captureTest'):
    os.mkdir(curdir + '\\screenShot\\captureTest')
print "screenShot folder created"


#创建截图的解释文件
filename2 = curdir + '/screenShot/captureTest/readme.txt'
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
print "excute case sets: 'captureTest status'"
f.write("**********************************************\n")
f.write("                 用例执行                       \n")
f.write("**********************************************\n\n")
f.flush()

#------------------------将转换后的自动化脚本复制到以下区域即可--------------------------------
##1、点击拍摄按钮，进入拍摄页面
##2、点击关闭按钮退出拍摄页面
##3、点击拍摄按钮进入拍摄页面
##4、长按拍摄按钮2秒
##5、长按拍摄按钮2秒
##6、点击会删
##7、长按拍摄按钮2秒
##8、点击两次回删
##9、点击确定按钮进入预览页面
##10、点击确定按钮，进入发布页面
##11、点击视频描述输入框
##12、输入hello
##13、点击保存草稿
##14、点击底导上的我，进入我的页面
##15、点击草稿箱
##16、点击缩略图，播放该草稿
##17、点击其他区域退出播放
##18、点击草稿，进入视频编辑页面
##19、点击确定按钮，进入发布页面
##20、点击发布
##21、点击关闭发布成功
##22、点击拍摄按钮，进入拍摄页面
##23、点击闪关灯
##24、点击前置摄像头
##25、点击切换到60秒拍摄
##26、点击拍摄按钮，拍摄20秒视频
##27、点击暂停拍摄
##28、点击确定按钮进入预览界面
##29、点击smile主题
##30、点击屏幕暂停播放
##31、点击确定按钮，进入预览界面
##32、点击发布
##33、点击关闭发布成功面板
##34、点击底导上的首页

##1、点击拍摄按钮，进入拍摄页面
##2、点击关闭按钮退出拍摄页面
##3、点击拍摄按钮进入拍摄页面
##4、长按拍摄按钮2秒
##5、长按拍摄按钮2秒
##6、点击会删
device.touch(378,1229,"DOWN_AND_UP")
writeToLog(f,"点击拍摄按钮，进入拍摄页面")
MonkeyRunner.sleep(2.0)
device.touch(49,48,"DOWN_AND_UP")
writeToLog(f,"点击关闭按钮退出拍摄页面")
MonkeyRunner.sleep(2.0)
device.touch(382,1229,"DOWN_AND_UP")
writeToLog(f,"点击拍摄按钮进入拍摄页面")
MonkeyRunner.sleep(2.0)
device.drag((357,1048),(357,1048),2,10)
writeToLog(f,"长按拍摄按钮2秒")
MonkeyRunner.sleep(2.0)
device.drag((351,1053),(351,1053),2,10)
writeToLog(f,"长按拍摄按钮2秒")
MonkeyRunner.sleep(2.0)
device.touch(110,1053,"DOWN_AND_UP")
writeToLog(f,"点击会删")
getPic(device,curdir,"captureTest",1)
writeToDetails(fi,"1、一段处于回删状态的视频截图")
MonkeyRunner.sleep(2.0)
device.touch(357,1048,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
##7、长按拍摄按钮2秒
##8、点击两次回删
device.drag((373,1040),(373,1040),2,10)
writeToLog(f,"长按拍摄按钮2秒")
MonkeyRunner.sleep(2.0)
device.touch(126,1037,"DOWN_AND_UP")
MonkeyRunner.sleep(1.0)
device.touch(121,1056,"DOWN_AND_UP")
writeToLog(f,"点击两次回删")
MonkeyRunner.sleep(2.0)
##9、点击确定按钮进入预览页面
device.touch(603,1037,"DOWN_AND_UP")
writeToLog(f,"点击确定按钮进入预览页面")
MonkeyRunner.sleep(5.0)
getPic(device,curdir,"captureTest",2)
writeToDetails(fi,"2、预览界面截图")
##10、点击确定按钮，进入发布页面
device.touch(666,45,"DOWN_AND_UP")
writeToLog(f,"点击确定按钮，进入发布页面")
MonkeyRunner.sleep(16.0)
getPic(device,curdir,"captureTest",3)
writeToDetails(fi,"3、发布页面截图")
##11、点击视频描述输入框
##12、输入hello
device.touch(256,477,"DOWN_AND_UP")
writeToLog(f,"点击视频描述输入框")
MonkeyRunner.sleep(4.0)
device.type("hello")
writeToLog(f,"输入hello")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"captureTest",4)
writeToDetails(fi,"4、发布页面输入hello截图")
##13、点击保存草稿
##14、点击底导上的我，进入我的页面
##15、点击草稿箱
##16、点击缩略图，播放该草稿
device.touch(648,45,"DOWN_AND_UP")
writeToLog(f,"点击保存草稿")
MonkeyRunner.sleep(3.0)
device.touch(654,1226,"DOWN_AND_UP")
writeToLog(f,"点击底导上的我，进入我的页面")
MonkeyRunner.sleep(2.0)
device.touch(654,98,"DOWN_AND_UP")
writeToLog(f,"点击草稿箱")
MonkeyRunner.sleep(3.0)
getPic(device,curdir,"captureTest",5)
writeToDetails(fi,"5、草稿箱页面截图")
device.touch(108,232,"DOWN_AND_UP")
writeToLog(f,"点击缩略图，播放该草稿")
MonkeyRunner.sleep(5.0)
getPic(device,curdir,"captureTest",6)
writeToDetails(fi,"6、草播放草稿箱视频截图")
##17、点击其他区域退出播放
##18、点击草稿，进入视频编辑页面
##19、点击确定按钮，进入发布页面
##20、点击发布
device.touch(238,157,"DOWN_AND_UP")
writeToLog(f,"点击其他区域退出播放")
MonkeyRunner.sleep(2.0)
device.touch(438,248,"DOWN_AND_UP")
writeToLog(f,"点击草稿，进入视频编辑页面")
MonkeyRunner.sleep(5.0)
device.touch(663,50,"DOWN_AND_UP")
writeToLog(f,"点击确定按钮，进入发布页面")
MonkeyRunner.sleep(16.0)
device.touch(355,1202,"DOWN_AND_UP")
writeToLog(f,"点击发布")
MonkeyRunner.sleep(10.0)
getPic(device,curdir,"captureTest",7)
writeToDetails(fi,"7、发布成功界面截图")
##21、点击关闭发布成功
##22、点击拍摄按钮，进入拍摄页面
##23、点击闪关灯
device.touch(639,642,"DOWN_AND_UP")
writeToLog(f,"点击关闭发布成功")
MonkeyRunner.sleep(2.0)
device.touch(378,1226,"DOWN_AND_UP")
writeToLog(f,"点击拍摄按钮，进入拍摄页面")
MonkeyRunner.sleep(2.0)
device.touch(510,53,"DOWN_AND_UP")
writeToLog(f,"点击闪关灯")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"captureTest",8)
writeToDetails(fi,"8、拍摄页面，闪光灯打开截图")
##24、点击前置摄像头
##25、点击切换到60秒拍摄
##26、点击拍摄按钮，拍摄20秒视频
##27、点击暂停拍摄
device.touch(659,45,"DOWN_AND_UP")
writeToLog(f,"点击前置摄像头")
MonkeyRunner.sleep(2.0)
device.touch(357,56,"DOWN_AND_UP")
writeToLog(f,"点击切换到60秒拍摄")
MonkeyRunner.sleep(2.0)
device.touch(371,1050,"DOWN_AND_UP")
writeToLog(f,"点击拍摄按钮，拍摄20秒视频")
MonkeyRunner.sleep(20.0)
device.touch(366,1045,"DOWN_AND_UP")
writeToLog(f,"点击暂停拍摄")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"captureTest",9)
writeToDetails(fi,"9、拍摄20秒视频截图")
##28、点击确定按钮进入预览界面
##29、点击smile主题
##30、点击屏幕暂停播放
device.touch(603,1053,"DOWN_AND_UP")
writeToLog(f,"点击确定按钮进入预览界面")
MonkeyRunner.sleep(10.0)
device.touch(488,1093,"DOWN_AND_UP")
writeToLog(f,"点击smile主题")
MonkeyRunner.sleep(15.0)
device.touch(346,509,"DOWN_AND_UP")
writeToLog(f,"点击屏幕暂停播放")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"captureTest",10)
writeToDetails(fi,"10、预览界面使用主题截图")
##31、点击确定按钮，进入预览界面
##32、点击发布
##33、点击关闭发布成功面板
##34、点击底导上的首页
device.touch(661,50,"DOWN_AND_UP")
writeToLog(f,"点击确定按钮，进入预览界面")
MonkeyRunner.sleep(60.0)
device.touch(346,1221,"DOWN_AND_UP")
writeToLog(f,"点击发布")
MonkeyRunner.sleep(20.0)
device.touch(639,642,"DOWN_AND_UP")
writeToLog(f,"点击关闭发布成功面板")
MonkeyRunner.sleep(2.0)
device.touch(51,1232,"DOWN_AND_UP")
writeToLog(f,"点击底导上的首页")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"captureTest",11)
writeToDetails(fi,"11、首页截图")

#------------------------将转换后的自动化脚本复制到以上区域即可--------------------------------


print "end..."
f.close()
fi.close
