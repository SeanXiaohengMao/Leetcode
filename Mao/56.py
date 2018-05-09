# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)<=1:
        	return intervals
        li = [(i.start,i.end) for i in intervals]
        li.sort()
        prev_s, prev_e = li[0][0], li[0][1]
        rl = []
        for i in li[1:]:
        	if i[0]>prev_e:
        		rl.append(Interval(prev_s, prev_e))
        		prev_s, prev_e = i[0], i[1]
        	else:
        		prev_e = max(i[1], prev_e)
        rl.append(Interval(prev_s, prev_e))
        return rl

# print Solution().merge([[1,3],[2,6],[8,10],[15,18]])

