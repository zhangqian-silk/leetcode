'''
    给定一个二叉树，原地将它展开为一个单链表。

    例如，给定二叉树

        1
       / \\
      2   5
     / \\  \\
    3   4    6
    将其展开为：

    1
     \\
      2
       \\
        3
         \\
          4
           \\
            5
             \\
              6

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        queue = []
        pre_root = None
        while root or queue:
            while root:
                queue.append(root)
                root = root.left
            root = queue[-1]
            if root.right is None or root.right == pre_root:
                if root.left:
                    last = root.left
                    while last.right:
                        last = last.right
                    last.right = root.right
                    root.right = root.left
                    root.left = None
                queue.pop(-1)
                pre_root = root
                root = None
            else:
                root = root.right
    


            
            


        
        