'''
    请判断一个链表是否为回文链表。

    示例 1:

    输入: 1->2
    输出: false

    示例 2:

    输入: 1->2->2->1
    输出: true

    进阶：
    你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/palindrome-linked-list
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        low = head
        quick = head
        pre_low = None
        nxt_low = low.next
        if nxt_low is None:
            return True
        while quick:
            quick = quick.next
            if quick:
                quick = quick.next
                low.next = pre_low
                pre_low = low
                low = nxt_low
                nxt_low = low.next
            # quick只走一步，说明链表节点为奇数个 1+2n+None
            # 此时low在中间,应该判断pre_low和nxt_low
            else:
                low = low.next
                break
        # 如果不是通过break退出，说明链表节点为偶数个 1+2n-1+None
        # 此时low为1+n，在中间两个节点的右侧，应该判断pre_low和low
        while pre_low:
            if pre_low.val == low.val:
                pre_low = pre_low.next
                low = low.next
            else:
                return False
        return True