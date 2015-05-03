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
filename = curdir + '/log/begin2Log.txt'  
f = open(filename,'w')
f.write("日志文件创建成功：       " + getTime())
f.flush()
print "create logfile success"


#创建截图存放的文件夹
if not os.path.exists(curdir + '\\screenShot\\unlogin'):
    os.mkdir(curdir + '\\screenShot\\unlogin')
print "screenShot folder created"


#创建截图的解释文件
filename2 = curdir + '/screenShot/unlogin/readme.txt'
fi = open(filename2,'w')
print "create screenshot details file success"


#安装apk
device.installPackage(curdir + '\\apk\\miaopai520.apk')
print "install successfully !"
print

#启动秒拍apk
package = 'com.yixia.videoeditor'
activity = 'com.yixia.videoeditor.ui.login.SplashActivity'
runComponent = package + '/' + activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(10.0)

#一下是正式的操作代码
print "start oparation ..."
print "**********************************************"
print "excute case sets: 'unlogin status'"
f.write("**********************************************\n")
f.write("         未登录情况用例执行                       \n")
f.write("**********************************************\n\n")
f.flush()

#------------------------将转换后的自动化脚本复制到以下区域即可--------------------------------
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

#引导页截图
getPic(device,curdir,"",1)
f.write("点引导页截图：       " + getTime())
print "**********************************************"
#跳过引导页
device.press("KEYCODE_BACK","DOWN_AND_UP")
MonkeyRunner.sleep(10.0)

#点击进入详情页并开始播放视频
device.touch(182,314,"DOWN_AND_UP")
f.write("点击进入详情页并开始播放视频：       " + getTime())
MonkeyRunner.sleep(10.0)
getPic(device,curdir,"unlogin",1)
writeToDetails(fi,"1、详情页面截图")
#点击停止播放
device.touch(389,650,"DOWN_AND_UP")
writeToLog(f,"点击停止播放：       ")
MonkeyRunner.sleep(2.0)

#点击加关注按钮
device.touch(641,205,"DOWN_AND_UP")
writeToLog(f,"点击加关注按钮：       ")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"unlogin",2)
writeToDetails(fi,"2、点击关注按钮，弹出登陆对话框截图")

#点击关闭登录对话框
device.touch(555,376,"DOWN_AND_UP")
writeToLog(f,"点击关闭登录对话框：       ")
MonkeyRunner.sleep(2.0)
#向上滑动
device.drag((288,1024),(288,724),1.0,10)
writeToLog(f,"向上滑动：       ")
MonkeyRunner.sleep(2.0)
#双击喜欢
device.touch(400,418,"DOWN_AND_UP")
device.touch(400,418,"DOWN_AND_UP")
writeToLog(f,"双击喜欢：       ")
MonkeyRunner.sleep(2.0)
#点击关闭登录对话框
device.touch(555,370,"DOWN_AND_UP")
writeToLog(f,"点击关闭登录对话框：       ")
MonkeyRunner.sleep(2.0)

#--------------------------------------------------------------------------------
###点击喜欢按钮
##device.touch(461,1034,"DOWN_AND_UP")
##writeToLog(f,"点击喜欢按钮：       ")
##MonkeyRunner.sleep(2.0)
###点击关闭登录对话框
##device.touch(560,373,"DOWN_AND_UP")
##writeToLog(f,"点击关闭登录对话框：       ")
##MonkeyRunner.sleep(2.0)
###点击分享
##device.touch(621,1024,"DOWN_AND_UP")\
##writeToLog(f,"点击分享：       ")
##MonkeyRunner.sleep(2.0)
###点击关闭登录对话框
##device.touch(555,376,"DOWN_AND_UP")
##writeToLog(f,"点击关闭登录对话框：       ")
##MonkeyRunner.sleep(2.0)
#--------------------------------------------------------------------------------
#点击发送按钮
device.touch(679,1224,"DOWN_AND_UP")
writeToLog(f,"点击发送按钮：       ")
MonkeyRunner.sleep(2.0)
#点击关闭登录对话框
device.touch(560,365,"DOWN_AND_UP")
writeToLog(f,"点击关闭登录对话框：       ")
MonkeyRunner.sleep(2.0)
#点击返回退出详情页面
device.touch(38,90,"DOWN_AND_UP")
writeToLog(f,"点击返回退出详情页面：       ")
MonkeyRunner.sleep(2.0)
#点击拍摄按钮
device.touch(366,1221,"DOWN_AND_UP")
writeToLog(f,"点击拍摄按钮：       ")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"unlogin",3)
writeToDetails(fi,"3、点击拍摄按钮，弹出登陆对话框截图")
#点击关闭登录对话框
device.touch(558,373,"DOWN_AND_UP")
writeToLog(f,"点击关闭登录对话框：       ")
MonkeyRunner.sleep(2.0)
#点击好友
device.touch(531,1232,"DOWN_AND_UP")
writeToLog(f,"点击好友：       ")
MonkeyRunner.sleep(2.0)
#点击立即登录
device.touch(393,706,"DOWN_AND_UP")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"unlogin",4)
writeToLog(f,"点击立即登录：       ")
writeToDetails(fi,"4、消息页面点击立即登陆按钮，弹出登陆对话框截图")
#点击关闭登录对话框
device.touch(560,376,"DOWN_AND_UP")
writeToLog(f,"点击关闭登录对话框：       ")
MonkeyRunner.sleep(2.0)
#点击我
device.touch(652,1229,"DOWN_AND_UP")
writeToLog(f,"点击我：       ")
MonkeyRunner.sleep(2.0)
#点击立即登录
device.touch(364,704,"DOWN_AND_UP")
writeToLog(f,"点击立即登录：       ")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"unlogin",5)
writeToDetails(fi,"5、我的页面点击立即登陆按钮，弹出登陆对话框截图")
#点击关闭登录对话框
device.touch(560,373,"DOWN_AND_UP")
writeToLog(f,"点击关闭登录对话框：       ")
MonkeyRunner.sleep(2.0)
#点击设置
device.touch(58,104,"DOWN_AND_UP")
writeToLog(f,"点击设置：       ")
MonkeyRunner.sleep(2.0)
#点击立即登录
device.touch(398,952,"DOWN_AND_UP")
writeToLog(f,"点击立即登录：       ")
MonkeyRunner.sleep(2.0)
getPic(device,curdir,"unlogin",6)
writeToDetails(fi,"6、设置页面点击立即登陆按钮，弹出登陆对话框截图")
#点击关闭登录对话框
device.touch(555,370,"DOWN_AND_UP")
writeToLog(f,"点击关闭登录对话框：       ")
MonkeyRunner.sleep(2.0)
#点击返回退出设置页面
device.touch(45,93,"DOWN_AND_UP")
writeToLog(f,"点击返回退出设置页面       ")
MonkeyRunner.sleep(2.0)
#点击首页
device.touch(63,1221,"DOWN_AND_UP")
writeToLog(f,"点击首页：       ")
MonkeyRunner.sleep(2.0)



#创建截图存放的文件夹
if not os.path.exists(curdir + '\\screenShot\\mobileLogin'):
    os.mkdir(curdir + '\\screenShot\\mobileLogin')
print "screenShot folder created"


#创建截图的解释文件
filename2 = curdir + '/screenShot/mobileLogin/readme.txt'
fi = open(filename2,'w')
print "create screenshot details file success"

print "**********************************************"
print "excute case sets: 'mobileLogin status'"
f.write("**********************************************\n")
f.write("          手机登陆用例执行                       \n")
f.write("**********************************************\n\n")
f.flush()

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
MonkeyRunner.sleep(2.0)

#创建截图存放的文件夹
if not os.path.exists(curdir + '\\screenShot\\settingTest'):
    os.mkdir(curdir + '\\screenShot\\settingTest')
print "screenShot folder created"


#创建截图的解释文件
filename2 = curdir + '/screenShot/settingTest/readme.txt'
fi = open(filename2,'w')
print "create screenshot details file success"

print "**********************************************"
print "excute case sets: 'settingTest status'"
f.write("**********************************************\n")
f.write("          设置页面用例执行                       \n")
f.write("**********************************************\n\n")
f.flush()

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


#创建截图存放的文件夹
if not os.path.exists(curdir + '\\screenShot\\commentTest'):
    os.mkdir(curdir + '\\screenShot\\commentTest')
print "screenShot folder created"


#创建截图的解释文件
filename2 = curdir + '/screenShot/commentTest/readme.txt'
fi = open(filename2,'w')
print "create screenshot details file success"

print "**********************************************"
print "excute case sets: 'commentTest status'"
f.write("**********************************************\n")
f.write("             评论用例执行                       \n")
f.write("**********************************************\n\n")
f.flush()

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

#创建截图存放的文件夹
if not os.path.exists(curdir + '\\screenShot\\searchTest'):
    os.mkdir(curdir + '\\screenShot\\searchTest')
print "screenShot folder created"


#创建截图的解释文件
filename2 = curdir + '/screenShot/searchTest/readme.txt'
fi = open(filename2,'w')
print "create screenshot details file success"

print "**********************************************"
print "excute case sets: 'searchTest status'"
f.write("**********************************************\n")
f.write("           搜索用例执行                       \n")
f.write("**********************************************\n\n")
f.flush()

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


#创建截图存放的文件夹
if not os.path.exists(curdir + '\\screenShot\\captureTest'):
    os.mkdir(curdir + '\\screenShot\\captureTest')
print "screenShot folder created"


#创建截图的解释文件
filename2 = curdir + '/screenShot/captureTest/readme.txt'
fi = open(filename2,'w')
print "create screenshot details file success"

print "**********************************************"
print "excute case sets: 'captureTest status'"
f.write("**********************************************\n")
f.write("           拍摄发布用例执行                      \n")
f.write("**********************************************\n\n")
f.flush()

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

print "uninstalling ......."
device.removePackage('com.yixia.videoeditor')
print "uninstalled"
print "end..."
f.close()
fi.close

