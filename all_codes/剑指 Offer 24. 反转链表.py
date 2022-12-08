'''
    定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

    示例:

    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL

    限制：

    0 <= 节点个数 <= 5000

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        pre_node = None
        cur_node = head
        next_node = head
        if next_node is None:
            return None
        else:
            next_node = next_node.next
        while next_node is not None:
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
            next_node = next_node.next
        cur_node.next = pre_node
        return cur_node
        
            