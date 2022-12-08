'''
    给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

    struct Node {
    int val;
    Node *left;
    Node *right;
    Node *next;
    }
    填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

    初始状态下，所有 next 指针都被设置为 NULL。

    进阶：

    你只能使用常量级额外空间。
    使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

    示例：

    输入：root = [1,2,3,4,5,6,7]
    输出：[1,#,2,3,#,4,5,6,7,#]
    解释：你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点。
    序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
     
    提示：

    树中节点的数量少于 4096
    -1000 <= node.val <= 1000

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def connect2(node1, node2):
            if node1 is None or node1.next is not None:
                return
            node1.next = node2
            connect2(node1.left, node1.right)
            connect2(node2.left, node2.right)
            connect2(node1.right, node2.left)
        if root is None:
            return None
        connect2(root.left, root.right)
        return root