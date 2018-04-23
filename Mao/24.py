# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        if node.next:
	        head = node.next
        while node:
	        if node.next:	
		        if node.next.next and node.next.next.next:
		        	nodeN = node.next.next
		        	nodeM = node.next.next.next
 		        	node.next.next = node
		        	node.next = nodeM
		        	node = nodeN
		        else:
		        	nodeN = node.next.next
		        	node.next.next = node
		        	node.next = nodeN
		        	node = nodeN
	        else:
	        	return head
        return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d= ListNode(4)

a.next = b
b.next = c 
c.next = d

head = Solution().swapPairs(a)
i = 0
while head:
	if i>10:
		break
	i+=1
	print head.val
	head = head.next
