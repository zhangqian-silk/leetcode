'''
    给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。

    进阶:
    如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？

    示例:

    // 初始化一个单链表 [1,2,3].
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(3);
    Solution solution = new Solution(head);

    // getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
    solution.getRandom();

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/linked-list-random-node
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from random import randint
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        i = 0
        list_node = self.head
        res = 0
        while list_node:
            rand_i = randint(0, i)
            if rand_i == i:
                res = list_node.val
            list_node = list_node.next
            i += 1
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()