#!/usr/bin/env python

import os

int_access = '<get_host_by_name socket='
sketchy_urls = ['ads.netbios-local.com', 'upd.host255-255-255-0.com', 'ads.range159-195.com']
VB = 'MSVBVM60'
sketchy_calls = set()

flag = 0
for fn in os.listdir('./train'):
	f = open('./train/'+fn, 'r')
	for line in f:
		for url in sketchy_urls:
			if url in line: flag = 1
		if int_access in line:
			sketchy_calls.add(line)
	if flag: print fn
	flag = 0
	f.close()
print sketchy_calls

