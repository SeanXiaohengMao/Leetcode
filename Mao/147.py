# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = newhead = ListNode(0)
        cur = newhead.next = head
        while cur and cur.next:
            v = cur.next.val
            if v >= cur.val:
                cur = cur.next
                continue
            if p.next.val >= v:
                p = newhead
            while v > p.next.val:
                p = p.next
            temp = cur.next.next
            cur.next.next = p.next
            p.next = cur.next
            cur.next = temp
        return newhead.next
            