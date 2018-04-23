# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return None
        
        slow = slow.next
        while head!=slow:
            head = head.next
            slow = slow.next
        return head
        # dict = {}
        # while head:
        #     if head in dict:
        #         return head
        #     dict[head] = 1
        #     head = head.next