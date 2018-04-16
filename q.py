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
	print ' finished: ', len(finished)
	if (sorted( set(q) - set(finished) ) == 0):
		print "All finished, Congratulation!!!\n"
	else:
		print ' unfinished: ', sorted( set(q) - set(finished) )

	return finished

# week 1
q = [1, 136, 3, 771, 535, 217, 149, 202, 138, 49, 463, 219, 760, 36, 85]
q += [2, 237, 21, 206, 23, 148, 141, 138, 328, 234, 160, 147, 142, 24, 19]

q = list(set(q))
q.sort()

print 'Total_Questions: ', len(set(q))

# Finished
m_finished = finished('Mao')
s_finished = finished('shadow')

