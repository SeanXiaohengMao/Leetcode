# ''' 
# Python File for Leetcode Question Schedule Follow Up
# Version: 0.1 
# '''

import sys
from os import listdir
from os.path import splitext

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
		f.write('\t unfinished: %s\n'%str(numlist))

	return finished

string = ''''''

f = open("README.md", "a+")
f.write(string)

# week 1
q = [1, 136, 3, 771, 535, 217, 149, 202, 138, 49, 463, 219, 760, 36, 85]
q += [2, 237, 21, 206, 23, 148, 141, 138, 328, 234, 160, 147, 142, 24, 19]

# week 2
# mao
q+ = [242, 347, 349, 500, 387, 336, 187, 204, 37, 76, 205, 18, 350, 30, 200, 279, 101, 127, 301, 102, 111, 133]
# fang
q+ = []
# liu
q+ = []

q = list(set(q))
q.sort()

print 'Total: ', len(set(q))
f.write('\tTotal: %d\n'%len(set(q)))

# Finished
m_finished = finished('Mao')
s_finished = finished('shadow')

f.close

