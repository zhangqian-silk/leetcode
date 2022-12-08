'''
    给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

    示例:

    输入: [1,2,3,null,5,null,4]
    输出: [1, 3, 4]
    解释:

      1            <---
    /   \\
    2     3         <---
    \\    \\
     5     4       <---

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur_queue = []
        nxt_queue = []
        all_res = []
        if root is None:
            return all_res
        while True:
            if root:
                if root.left:
                    nxt_queue.append(root.left)
                if root.right:
                    nxt_queue.append(root.right)
                res = root.val
            if cur_queue:
                root = cur_queue.pop(0)
            elif nxt_queue:
                all_res.append(res)
                cur_queue = nxt_queue[:]
                nxt_queue =[]
                root = cur_queue.pop(0)
            else:
                break
        all_res.append(res)
        return all_res