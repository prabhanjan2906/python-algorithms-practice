class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        # if (not t1 or not t2):
            # return t1 or t2

        # t1.val = t1.val + t2.val
        # if (t1.left and t2.left):
        #     t1 =  self.mergeTrees(t1.left, t2.left)
        # if (t1.right and t2.right):
        #     t1 = self.mergeTrees(t1.right, t2.right)
        # if (t2.left and not t1.left):
        #     t1.left = t2.left
        #     t2.left = None
        # if (not t1.right and t2.right):
        #     t1.right = t2.right
        #     t2.right = None
        # return t1

        if (not t1 or not t2):
            return t1 or t2

        t1.val = t1.val + t2.val
        t1.left = mergeTrees(t1.left, t2.left)
        t1.right = mergeTrees(t1.right, t2.right)
        return t1