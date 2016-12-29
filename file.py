#!/usr/bin/python

import os
import time

source = ['/Users/linfang/Documents/learning/small_test']

target_dir = '/Users/linfang/Documents/learning/server/python/'

today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully created directory', today

target = today + os.sep + now + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print 'Successful backup to', target
else :
	'Successful backup to', target

