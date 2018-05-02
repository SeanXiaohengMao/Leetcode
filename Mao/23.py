# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
        	return None
        while len(lists)>1:
	        lists.append(self.merge(lists.pop(), lists.pop()))
        return lists[0]

    def merge(self, a, b):
    	dummy = tail = ListNode(0)
    	while a and b:
    		if a.val < b.val:
    			tail.next = a
    			tail = tail.next
    			a = a.next
    		else:
    			tail.next = b
    			tail = tail.next
    			b = b.next

    	tail.next = a or b
    	return dummy.next