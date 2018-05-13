# '''
# Python File for Leetcode Question Schedule Follow Up
<<<<<<< HEAD
# Version: 0.2
=======
# Version: 0.1
>>>>>>> f127029c0cca20dc5cb5d5f4e8f6bf1ed04dff0b
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

<<<<<<< HEAD
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
=======
# week 1
q = [1, 136, 3, 771, 535, 217, 149, 202, 138, 49, 463, 219, 760, 36, 85]
q += [2, 237, 21, 206, 23, 148, 141, 138, 328, 234, 160, 147, 142, 24, 19]

# week 2
# mao
q += [242, 347, 349, 500, 387, 336, 187, 204, 37, 76, 205, 18, 350, 30, 200, 279, 101, 127, 301, 102, 111, 133]
# fang
q += [104, 226, 617, 100, 173, 96, 110, 101, 669, 236, 654, 99, 109, 222, 257, 114, 94, 543, 199, 144]
# liu
q += [143, 83, 445, 203, 109, 25, 92, 86, 61, 82, 4, 11, 561, 66, 122, 53, 169, 283, 121, 42]
>>>>>>> f127029c0cca20dc5cb5d5f4e8f6bf1ed04dff0b

q = list(set(q))
q.sort()

print 'Total: ', len(set(q))
f.write('\tTotal: %d\n'%len(set(q)))

# Finished
m_finished = finished('Mao')
s_finished = finished('shadow')

f.close
