# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            slownxt = slow.next
            slow.next = node
            node = slow
            slow = slownxt
        node1 = head
        while node1 and node:
            if node.val != node1.val:
                return False
            node = node.next
            node1 = node1.next
        return True