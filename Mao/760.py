class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dic = {}
        li = []
        for i, num in enumerate(B):
        	if num in dic:
        		dic[num].append(i)
        	else:
        		dic[num] = [i]
        for num in A:
        	li.append(dic[num].pop())
        return li

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
print Solution().anagramMappings(A, B)