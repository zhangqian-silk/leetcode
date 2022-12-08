'''
    给定一个二叉树，找出其最小深度。

    最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

    说明：叶子节点是指没有子节点的节点。

    示例：

    输入：root = [3,9,20,null,null,15,7]
    输出：2

    提示：

    树中节点数的范围在 [0, 105] 内
    -1000 <= Node.val <= 1000

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS 用队列实现
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = []
        queue.append(root)
        lenth = 1
        while queue:
            size = len(queue)
            i = 0
            while i < size:
                i += 1
                tnode = queue.pop(0)
                if tnode is not None:
                    if (tnode.left is None) and (tnode.right is None):
                        return lenth
                    else:
                        queue.append(tnode.left)
                        queue.append(tnode.right)
            lenth += 1

