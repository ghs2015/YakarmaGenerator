from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import random

print ('waiting for device')
device = MonkeyRunner.waitForConnection()
print ('device attached')

device.installPackage('myproject/bin/MyApplication.apk')

# sets a variable with the package's internal name
package = 'com.example.android.myapplication'

# sets a variable with the name of an Activity in the package
activity = 'com.example.android.myapplication.MainActivity'

# sets the name of the component to start
runComponent = package + '/' + activity

# Runs the component
device.startActivity(component=runComponent)


f = open("crawled.txt", "r")
yak = f.readlines()
f.close()


def process(yak):

	device.touch( 970, 160 , MonkeyDevice.DOWN_AND_UP)
	print('touched1')
	time.sleep(0.5)
	device.touch(300, 400, MonkeyDevice.DOWN_AND_UP)
	print('touched2')
	time.sleep(0.5)

	splits=yak.split()
	for z in splits:
		device.type(z)
		device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)

	print('text added')
	time.sleep(0.5)
	device.touch( 970 , 160, MonkeyDevice.DOWN_AND_UP)


def contains(yak1, lst):
	for k in lst:
		if yak1 == k:
			return False
	return True


randnum = random.randint(0, len(yak))
g = open("posted.txt", "a")
g.write('new post' + '\n')


h = open("posted.txt", "r")
check = h.readlines()
h.close()

while contains(yak[randnum], check) == False:
	randnum = random.randint(0, len(yak)-1)



g.write(yak[randnum])
process(yak[randnum])