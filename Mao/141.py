# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
	        slow = head
	        fast = head.next
	        while slow != fast:
	        	slow = slow.next
	        	fast = fast.next.next
	        return True
        except:
	    	return False

head = ListNode(5)
head.next = ListNode(3)
head.next.next = ListNode(4)
print Solution().hasCycle(head)