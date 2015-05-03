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
filename = curdir + '/log/settingTestLog.txt'  
f = open(filename,'w')
f.write("日志文件创建成功：       " + getTime())
f.flush()
print "create logfile success"


#创建截图存放的文件夹
if not os.path.exists(curdir + '\\screenShot\\settingTest'):
    os.mkdir(curdir + '\\screenShot\\settingTest')
print "screenShot folder created"


#创建截图的解释文件
filename2 = curdir + '/screenShot/settingTest/readme.txt'
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
print "excute case sets: 'settingTest status'"
f.write("**********************************************\n")
f.write("                 用例执行                       \n")
f.write("**********************************************\n\n")
f.flush()

#------------------------将转换后的自动化脚本复制到以下区域即可--------------------------------
##1、点击地道底部导航上的“我”
##2、在我的页面点击设置按钮（进入设置页面）
##3、打开wifi下自动播放
##4、打开“3G拍摄下使用较低画质”
##5、打开静音
##6、点击新消息提醒，进入新消息提醒页面
##7、关闭新粉丝push
##8、关闭评论push
##9、关闭喜欢push
##10、点击反回，回到设置页面
##11、关闭wifi下自动播放
##12、关闭“3G拍摄下使用较低画质”
##13、关闭静音
##14、点击新消息提醒，进入新消息提醒页面
##15、打开新粉丝push
##16、打开评论push
##17、打开喜欢push
##18、点击反回，回到设置页面
##19、点击清空缓存
##20、点击“否”取消清空
##21、点击清空缓存
##22、点击“是”，清空缓存
##23、点击意见反馈，进入意见反馈页面
##24、什么也不输入、点击发送
##25、点击意见输入框
##26、输入“hello”
##27、点击“发送”
##28、点击意见反馈
##29、点击意见输入框
##30、输入“hello”
##31、点击联系方式输入框
##32、输入错误的邮箱地址
##33、点击发送
##34、点击联系方式输入框
##35、输入正确的邮箱地址
##36、点击发送
##37、点击意见反馈
##38、点击意见输入框
##39、输入“hello”
##40、点击联系方式输入框
##41、输入小于5位的qq号码
##42、点击发送
##43、点击联系方式输入框
##44、输入5为的qq号码
##45、点击发送
##46、点击返回按钮退出设置页面
##47、点击底导上的首页，进入首页

##1、点击地道底部导航上的“我”
##2、在我的页面点击设置按钮（进入设置页面）
device.touch(652,1234,"DOWN_AND_UP")
writeToLog(f,"点击地道底部导航上的“我”")
MonkeyRunner.sleep(2.0)
device.touch(58,90,"DOWN_AND_UP")
writeToLog(f,"在我的页面点击设置按钮（进入设置页面）")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"settingTest",1)
writeToDetails(fi,"1、设置页面截图")
##3、打开wifi下自动播放
##4、打开“3G拍摄下使用较低画质”
##5、打开静音
device.touch(634,229,"DOWN_AND_UP")
writeToLog(f,"打开wifi下自动播放")
MonkeyRunner.sleep(2.0)
device.touch(643,338,"DOWN_AND_UP")
writeToLog(f,"打开“3G拍摄下使用较低画质”")
MonkeyRunner.sleep(2.0)
device.touch(639,437,"DOWN_AND_UP")
writeToLog(f,"打开静音")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"settingTest",2)
writeToDetails(fi,"2、设置页面打开wifi下自动播放、3G拍摄较低画质、静音截图")
##6、点击新消息提醒，进入新消息提醒页面
##7、关闭新粉丝push
##8、关闭评论push
##9、关闭喜欢push
device.touch(639,530,"DOWN_AND_UP")
writeToLog(f,"点击新消息提醒，进入新消息提醒页面")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"settingTest",3)
writeToDetails(fi,"3、新消息提醒页面截图")
device.touch(627,248,"DOWN_AND_UP")
writeToLog(f,"关闭新粉丝push")
MonkeyRunner.sleep(2.0)
device.touch(632,354,"DOWN_AND_UP")
writeToLog(f,"关闭评论push")
MonkeyRunner.sleep(2.0)
device.touch(627,453,"DOWN_AND_UP")
writeToLog(f,"关闭喜欢push")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"settingTest",4)
writeToDetails(fi,"4、新消息提醒页面关闭新粉丝push、评论push、喜欢push截图")
##10、点击反回，回到设置页面
##11、关闭wifi下自动播放
##12、关闭“3G拍摄下使用较低画质”
##13、关闭静音
device.touch(38,98,"DOWN_AND_UP")
writeToLog(f,"点击反回，回到设置页面")
MonkeyRunner.sleep(2.0)
device.touch(623,229,"DOWN_AND_UP")
writeToLog(f,"关闭wifi下自动播放")
MonkeyRunner.sleep(2.0)
device.touch(627,336,"DOWN_AND_UP")
writeToLog(f,"关闭“3G拍摄下使用较低画质”")
MonkeyRunner.sleep(2.0)
device.touch(627,432,"DOWN_AND_UP")
writeToLog(f,"关闭静音")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"settingTest",5)
writeToDetails(fi,"5、设置页面关闭wifi下自动播放、3G拍摄较低画质、静音截图")
##14、点击新消息提醒，进入新消息提醒页面
##15、打开新粉丝push
##16、打开评论push
##17、打开喜欢push
device.touch(643,530,"DOWN_AND_UP")
writeToLog(f,"点击新消息提醒，进入新消息提醒页面")
MonkeyRunner.sleep(2.0)
device.touch(632,264,"DOWN_AND_UP")
writeToLog(f,"打开新粉丝push")
MonkeyRunner.sleep(2.0)
device.touch(623,357,"DOWN_AND_UP")
writeToLog(f,"打开评论push")
MonkeyRunner.sleep(2.0)
device.touch(627,461,"DOWN_AND_UP")
writeToLog(f,"打开喜欢push")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"settingTest",6)
writeToDetails(fi,"6、新消息提醒页面打开新粉丝push、评论push、喜欢push截图")
##18、点击反回，回到设置页面
##19、点击清空缓存
##20、点击“否”取消清空
##21、点击清空缓存
##22、点击“是”，清空缓存
device.touch(40,93,"DOWN_AND_UP")
writeToLog(f,"点击反回，回到设置页面")
MonkeyRunner.sleep(2.0)
device.touch(625,882,"DOWN_AND_UP")
writeToLog(f,"点击清空缓存")
MonkeyRunner.sleep(2.0)
device.touch(225,754,"DOWN_AND_UP")
writeToLog(f,"点击“否”取消清空")
MonkeyRunner.sleep(2.0)
device.touch(641,888,"DOWN_AND_UP")
writeToLog(f,"点击清空缓存")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"settingTest",7)
writeToDetails(fi,"7、清空缓存弹出对话框截图")
device.touch(535,733,"DOWN_AND_UP")
writeToLog(f,"点击“是”，清空缓存")
MonkeyRunner.sleep(2.0)
##23、点击意见反馈，进入意见反馈页面
##24、什么也不输入、点击发送
##25、点击意见输入框
##26、输入“hello”
##27、点击“发送”
device.touch(663,661,"DOWN_AND_UP")
writeToLog(f,"点击意见反馈，进入意见反馈页面")
MonkeyRunner.sleep(2.0)
device.touch(663,96,"DOWN_AND_UP")
writeToLog(f,"什么也不输入、点击发送")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"settingTest",8)
writeToDetails(fi,"8、意见反馈什么也不输入，点击发送的弹出toast提示")
device.touch(157,192,"DOWN_AND_UP")
writeToLog(f,"点击意见输入框")
MonkeyRunner.sleep(2.0)
device.type("hello")
writeToLog(f,"输入“hello”")
MonkeyRunner.sleep(2.0)
device.touch(670,101,"DOWN_AND_UP")
writeToLog(f,"点击“发送”")
MonkeyRunner.sleep(2.0)
##28、点击意见反馈
##29、点击意见输入框
##30、输入“hello”
##31、点击联系方式输入框
##32、输入错误的邮箱地址
##33、点击发送
device.touch(661,656,"DOWN_AND_UP")
writeToLog(f,"点击意见反馈")
MonkeyRunner.sleep(2.0)
device.touch(344,192,"DOWN_AND_UP")
writeToLog(f,"点击意见输入框")
MonkeyRunner.sleep(2.0)
device.type("hello")
writeToLog(f,"输入“hello”")
MonkeyRunner.sleep(2.0)
device.touch(72,480,"DOWN_AND_UP")
writeToLog(f,"点击联系方式输入框")
MonkeyRunner.sleep(2.0)
device.type("yiixia66")
writeToLog(f,"输入错误的邮箱地址")
MonkeyRunner.sleep(2.0)
device.touch(661,96,"DOWN_AND_UP")
writeToLog(f,"点击发送")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"settingTest",9)
writeToDetails(fi,"9、意见反馈输入错误的邮箱地址，点击发送的弹出toast提示")
##34、点击联系方式输入框
##35、输入正确的邮箱地址
##36、点击发送
device.touch(580,501,"DOWN_AND_UP")
writeToLog(f,"点击联系方式输入框")
MonkeyRunner.sleep(2.0)
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
MonkeyRunner.sleep(0.3)
device.press("KEYCODE_DEL","DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
device.type("yiixia66@163.com")
writeToLog(f,"输入正确的邮箱地址")
MonkeyRunner.sleep(2.0)
device.touch(661,96,"DOWN_AND_UP")
writeToLog(f,"点击发送")
MonkeyRunner.sleep(5.0)
##37、点击意见反馈
##38、点击意见输入框
##39、输入“hello”
##40、点击联系方式输入框
##41、输入小于5位的qq号码
##42、点击发送
device.touch(639,658,"DOWN_AND_UP")
writeToLog(f,"点击意见反馈")
MonkeyRunner.sleep(2.0)
device.touch(249,194,"DOWN_AND_UP")
writeToLog(f,"点击意见输入框")
MonkeyRunner.sleep(2.0)
device.type("hello")
writeToLog(f,"输入“hello”")
MonkeyRunner.sleep(2.0)
device.touch(348,504,"DOWN_AND_UP")
writeToLog(f,"点击联系方式输入框")
MonkeyRunner.sleep(2.0)
device.type("1234")
writeToLog(f,"输入小于5位的qq号码")
MonkeyRunner.sleep(2.0)
device.touch(661,93,"DOWN_AND_UP")
writeToLog(f,"点击发送")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"settingTest",10)
writeToDetails(fi,"10、意见反馈输入小于5位的qq号码，点击发送的弹出toast提示")
##43、点击联系方式输入框
##44、输入5为的qq号码
##45、点击发送
##46、点击返回按钮退出设置页面
##47、点击底导上的首页，进入首页
device.touch(330,498,"DOWN_AND_UP")
writeToLog(f,"点击联系方式输入框")
MonkeyRunner.sleep(2.0)
device.type("5")
writeToLog(f,"输入5为的qq号码")
MonkeyRunner.sleep(2.0)
device.touch(659,96,"DOWN_AND_UP")
writeToLog(f,"点击发送")
MonkeyRunner.sleep(5.0)
device.touch(38,93,"DOWN_AND_UP")
writeToLog(f,"点击返回按钮退出设置页面")
MonkeyRunner.sleep(2.0)
device.touch(65,1224,"DOWN_AND_UP")
writeToLog(f,"点击底导上的首页，进入首页")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"settingTest",11)
writeToDetails(fi,"11、首页截图")
MonkeyRunner.sleep(2.0)

#------------------------将转换后的自动化脚本复制到以上区域即可--------------------------------


print "end..."
f.close()
fi.close
