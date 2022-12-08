'''
    给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

    例如：
    给定二叉树 [3,9,20,null,null,15,7],

        3
    / \
    9  20
        /  \
    15   7
    返回锯齿形层次遍历如下：

    [
    [3],
    [20,9],
    [15,7]
    ]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cur_queue = []
        nxt_queue = []
        res = []
        all_res = []
        i = 1
        while True:
            if root:
                res.append(root.val)
                # 奇数层从左到右遍历
                if i % 2 == 1:
                    nxt_queue.append(root.left)
                    nxt_queue.append(root.right)
                # 偶数层从右到左遍历
                elif i % 2 == 0:
                    nxt_queue.append(root.right)
                    nxt_queue.append(root.left)
            if cur_queue:
                root = cur_queue.pop(0)
            # 当前层次遍历完成
            elif nxt_queue:
                all_res.append(res)
                res = []
                cur_queue = nxt_queue[::-1]
                nxt_queue = []
                i += 1
                root = cur_queue.pop(0)
            else:
                break
        return all_res
            
