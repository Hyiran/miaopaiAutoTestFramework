#coding=utf-8
import sys

print "###############################################"
print
print "          start run automatic script           "
print
print "###############################################"
print "----start----"
print "installing ......."


curdir = sys.argv[0]
index = curdir.rfind("\\")
curdir = curdir[:index]

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection()
device.installPackage(curdir + '\\apk\miaopai510.apk')
print "install successfully !"
print

package = 'com.yixia.videoeditor'
activity = 'com.yixia.videoeditor.ui.login.SplashActivity'
runComponent = package + '/' + activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(10.0)

result = device.takeSnapshot()
result.writeToFile(curdir + '\\screenShot\yingdaotu.png','png')
print "end screenshot: yingdaotu.png"
MonkeyRunner.sleep(1.0)

device.drag((384,341),(76,341),1.0,10)
MonkeyRunner.sleep(5.0)

#------------------------将转换后的自动化脚本复制到以下区域即可--------------------------------





#将转换后的自动化脚本复制与此处及可





#------------------------将转换后的自动化脚本复制到以上区域即可--------------------------------

print "uninstalling ......."
device.removePackage('com.yixia.videoeditor')
print "uninstalled"

