'''
    给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 
    如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

    说明：不允许修改给定的链表。

    进阶：

    你是否可以使用 O(1) 空间解决此题？
     
    示例 1：

    输入：head = [3,2,0,-4], pos = 1
    输出：返回索引为 1 的链表节点
    解释：链表中有一个环，其尾部连接到第二个节点。

    示例 2：

    输入：head = [1,2], pos = 0
    输出：返回索引为 0 的链表节点
    解释：链表中有一个环，其尾部连接到第一个节点。

    示例 3：

    输入：head = [1], pos = -1
    输出：返回 null
    解释：链表中没有环。
     
    提示：

    链表中节点的数目范围在范围 [0, 104] 内
    -105 <= Node.val <= 105
    pos 的值为 -1 或者链表中的一个有效索引

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        quick = head
        flag = False
        
        # 快慢指针判断环是否存在
        while True:
            if quick:
                quick = quick.next
            else:
                break
            if quick:
                quick = quick.next
            else:
                break
            slow = slow.next
            if slow == quick:
                flag = True
                break
        if flag:
            # 存在环的情况下，快指针比慢指针多走一圈
            # 此时快指针到环入口的距离，等于头节点到入口的距离
            slow = head
            while True:
                if slow == quick:
                    return slow
                slow = slow.next
                quick = quick.next
        else:
            return None