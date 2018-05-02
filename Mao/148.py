# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def merge(self, h1, h2):
		dummy = tail = ListNode(0)
		while h1 and h2:
			if h1.val < h2.val:
				tail.next = h1
				tail = tail.next
				h1 = h1.next
			else:
				tail.next = h2
				tail = tail.next
				h2 = h2.next

		tail.next = h1 if h1 else h2
		return dummy.next


	def sortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next:
			return head

		slow = fast = head
		pre = None
		while fast and fast.next:
			pre = slow
			fast = fast.next.next
			slow = slow.next

		pre.next = None
		return self.merge(*map(self.sortList, [head, slow]))