'''
    给定一个二叉树的根节点 root ，返回它的 中序 遍历。

    示例：

    输入：root = [1,null,2,3]
    输出：[1,3,2]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        res = []
        while root or queue:
            while root:
                queue.append(root)
                root = root.left
            root = queue.pop(-1)
            res.append(root.val)
            root = root.right
        return res