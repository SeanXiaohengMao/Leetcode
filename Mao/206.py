# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        node_prev = None
        while node:
        	noden = node.next
        	node.next = node_prev
        	node_prev = node
        	node = noden
        return node_prev