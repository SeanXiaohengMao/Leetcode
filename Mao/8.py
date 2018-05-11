class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        value = 0
        sign = 0
        minus = 0
        dic = {x:int(x) for x in '0123456789'}
        INT_MIN = -2**31
        INT_MAX = 2**31-1
        for i in str:
        	if i!=' ':
        		if i!='-' and i!='+':
        			if i>='0' and i<='9':
        				value = value*10+dic[i]
        				sign = 1
        				if minus == 0:
        					minus = 1
        			else:
        				break
        		elif minus == 0:
        			if i=='-':
        				minus = -1
        			else:
        				minus = 1
        			sign = 1
        		else:
        			break
        	elif sign:
        		break
        rv = int(minus)*value
        if rv<INT_MIN:
        	return INT_MIN
        if rv>INT_MAX:
        	return INT_MAX
        return rv

print Solution().myAtoi("0-1")