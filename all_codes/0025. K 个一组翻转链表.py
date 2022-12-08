'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        i = 1
        next_begin = head
        # k个一组，翻转前的最后一个节点，是翻转后的第一个节点
        while next_begin is not None and i < k:
            next_begin = next_begin.next
            i += 1
        if i < k:
            return head
        pre_node = None
        cur_node = head
        next_node = cur_node.next
        # k个一组，翻转前的第一个节点，是翻转后的最后一个节点
        cur_end = cur_node
        head = next_begin
        
        while next_begin is not None:
            i = 0
            # 翻转k个节点
            while i < k:
                cur_node.next = pre_node
                pre_node = cur_node
                cur_node = next_node
                next_node = cur_node.next 
                i += 1
            
            i = 1
            # 是否还有k个节点可以翻转
            next_begin = cur_node
            while next_begin is not None and i < k:
                next_begin = next_begin.next
                i += 1
            # 还存在需要反转的链表节点
            if next_begin is not None:
                cur_end.next = next_begin
                cur_end = cur_node
            # 不需要反转了
            elif next_begin is None:
                cur_end.next = cur_node
        return head
            

            