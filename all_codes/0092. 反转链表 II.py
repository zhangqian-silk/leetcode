'''
    反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

    说明:
    1 ≤ m ≤ n ≤ 链表长度。

    示例:

    输入: 1->2->3->4->5->NULL, m = 2, n = 4
    输出: 1->4->3->2->5->NULL

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        if head is None:
            return None
        if m == n:
            return head
        
        i = 1
        m_node = head
        pre_m_node = None
        while i < m:
            i += 1
            pre_m_node = m_node
            m_node = m_node.next
        # 循环结束后，pre_m_node指向第m-1个， 要指向第n个节点
        # m_node指向第m个节点，要指向第n+1个节点

        # 从第m+1个节点开始反转
        pre_node = m_node
        cur_node = pre_node.next
        next_node = cur_node.next
        i += 1

        # 反转循环结束，cur_node指向第n个结点
        while i < n:
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
            next_node = next_node.next
            i += 1
        cur_node.next = pre_node
        
        # 判断第m-1个节点是不是None
        if pre_m_node is None:
            m_node.next = next_node
            head = cur_node
        else:
            pre_m_node.next = cur_node
            m_node.next = next_node
       
        return head