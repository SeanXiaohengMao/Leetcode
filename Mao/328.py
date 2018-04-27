# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        if not head:
        	return head
        fast = head.next
        while fast and fast.next:
        	fnxt = fast.next
        	fnxttemp = fnxt.next

    		temp = slow.next
    		slow.next = fnxt
    		fnxt.next = temp
    		fast.next = fnxttemp
    		slow = slow.next

        	fast = fast.next
        return head

a = ListNode(2)
b = ListNode(1)
c = ListNode(3)
d = ListNode(5)
e = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
head = Solution().oddEvenList(a)
print head.val, head.next.val, head.next.next.val, head.next.next.next.val, head.next.next.next.next.val