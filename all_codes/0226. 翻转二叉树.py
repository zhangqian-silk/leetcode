'''
    翻转一棵二叉树。

    示例：

    输入：

        4
      /   \\
     2     7
    / \\  / \\
   1   3 6   9
    输出：

        4
      /   \\
     7     2
    / \\  / \\
   9   6 3   1

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/invert-binary-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def func(root):
            if root is None:
                return None
            
            temp = root.left
            root.left = func(root.right)
            root.right = func(temp)

            return root
        return func(root)
