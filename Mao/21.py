# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = node = ListNode(0)
        while l1 and l2:
        	if l1.val < l2.val:
        		node_tmp = l1
        		l1 = l1.next
        	else:
        		node_tmp = l2
        		l2 = l2.next
        	node.next = node_tmp
        	node = node.next
        node.next = l1 or l2
        return head.next

a = ListNode(1)
b = ListNode(2)
a.next = b
c = ListNode(1)
d = ListNode(3)
c.next = d
head = Solution().mergeTwoLists(a, c)
while head:
	print head.val
	head = head.next