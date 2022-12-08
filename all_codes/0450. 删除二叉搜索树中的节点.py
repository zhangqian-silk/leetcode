'''
    给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，
    并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

    一般来说，删除节点可分为两个步骤：

    首先找到需要删除的节点；
    如果找到了，删除它。
    说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

    示例:

    root = [5,3,6,2,4,null,7]
    key = 3

        5
       / \\
      3   6
     / \\  \\
    2   4   7

    给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

    一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

        5
       / \\
      4   6
     /     \\
    2       7

    另一个正确答案是 [5,2,6,null,4,null,7]。

        5
       / \\
      2   6
       \\  \\
        4   7

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        def find_min(root):
            while root.left:
                root = root.left
            return root
        def func(root, key):
            if root is None:
                return None
            if root.val == key:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                # 把右子树的最小值移动到该节点处
                else:
                    new_node = find_min(root.right)
                    new_node.left = root.left
                    new_node.right = func(root.right, new_node.val)
                    return new_node
            elif root.val > key:
                root.left = func(root.left, key)
            elif root.val < key:
                root.right = func(root.right, key)
            return root
        return func(root, key)