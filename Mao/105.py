# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
        	return None
        root = TreeNode(preorder[0])
        ind = inorder.index(preorder[0])
        left_in = inorder[:ind]
        right_in = inorder[ind+1:]
        left_pre = preorder[1:ind+1]
        right_pre = preorder[ind+1:]
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)
        return root