# '''
# Python File for Leetcode Question Schedule Follow Up
# Version: 0.2
# '''

import sys
from os import listdir
from os.path import splitext
import re


global q

def finished(dir):
	finished = []
	for i in listdir('./'+dir):
		i_temp = splitext(i)[0]
		if i_temp.isdigit():
			finished.append(int(i_temp))

	print dir+':'
	f.write('\t'+dir+':\n')
	print ' finished: ', len(finished)
	f.write('\t finished: %d\n'%len(finished))
	if (sorted( set(q) - set(finished) ) == 0):
		print "All finished, Congratulation!!!\n"
		f.write("\tAll finished!!!\n")
	else:
		numlist = sorted( set(q) - set(finished) )
		print ' unfinished: ', numlist
		print ' unfinished number: ', len(numlist)
		f.write('\t unfinished: %s\n'%str(numlist))
		f.write('\t unfinished number: %s\n'%str(len(numlist)))

	return finished

string = ''''''

f = open("README.md", "a+")
f.write(string)

# Add. questions
q = []

# Read Questions From File
f0 = open("README.md", "r")
for line in f0:
	matchObj = re.match( r'\s*[M|F|L]:([\d\s,]*)', line, re.M|re.I)
	if matchObj:
		arr = matchObj.group(1).split(',')
		for i in arr:
			matchObj_i = re.match( r'\s*(\d*).*', i, re.M|re.I)
			new = matchObj_i.group(1)
			if new.isdigit():
				q.append(int(new))
f0.close()

q = list(set(q))
q.sort()

print 'Total: ', len(set(q))
f.write('\tTotal: %d\n'%len(set(q)))

# Finished
m_finished = finished('Mao')
s_finished = finished('shadow')

f.close
