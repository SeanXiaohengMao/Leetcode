class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for st in strs:
        	st_set = tuple(sorted(st))
        	try:
        		dic[st_set].append(st)
        	except:
        		dic[st_set] = [st]
        return dic.values()

print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])