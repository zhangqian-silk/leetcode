'''
    给定一个二叉树，返回它的 后序 遍历。

    示例:

    输入: [1,null,2,3]  
    1
        \
        2
        /
    3 

    输出: [3,2,1]
    进阶: 递归算法很简单，你可以通过迭代算法完成吗？

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        res = []
        pre_root = None
        while root or queue:
            while root:
                queue.append(root)
                root = root.left
            root = queue[-1]
            if root.right is None or root.right == pre_root:
                res.append(root.val)
                queue.pop(-1)
                pre_root = root
                root = None
            else:
                root = root.right
        return res            