class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows >= len(s) or numRows == 1:
            return s
        temp = ['' for _ in range(numRows) ]
        step = 1
        i = 0
        
        for c in s:
            temp[i] += c
            if i==0:
                step = 1
            if i==numRows-1:
                step = -1
            i+= step
            
        return ''.join(temp)