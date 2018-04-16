def deleteDuplicated(list):
        resultList = []
        for item in list:
                if not item in resultList:
                        resultList.append(item)
        return resultList

# week 1
q = [1, 136, 3, 771, 535, 217, 149, 202, 138, 49, 463, 219, 760, 36, 85]
q += [2, 237, 21, 206, 23, 148, 141, 138, 328, 234, 160, 147, 142, 24, 19]

q = deleteDuplicated(q)
q.sort()

# Finished
m_finished = []

print 'Mao unfinished: ', sorted( set(q) - set(m_finished) )
print 'Total_len: ', len(set(q))

