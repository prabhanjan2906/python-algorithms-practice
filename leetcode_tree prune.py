# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if (root == None):
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if (root.left == None) and (root.right == None):
            if (root.val == 0):
                return None
        return root