# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodea = headA
        nodeb = headB

        while nodea != nodeb:
		        nodea = headB if not nodea else nodea.next
	        	nodeb = headA if not nodeb else nodeb.next
        return nodea