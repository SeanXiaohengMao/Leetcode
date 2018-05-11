# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
f = s = None
p = TreeNode(-1000000000)
class Solution(object):
    def traverse(root):
    	global f, s, p
    	if root == None:
    		return
    	traverse(root.left)
    	if f==None and p.val>=root.val:
    		f = p
    		# print f.val
    	if f!=None and p.val>=root.val:
    		s = root
    	p = root
    	traverse(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        print f.val,s.val
        f.val, s.val = s.val, f.val