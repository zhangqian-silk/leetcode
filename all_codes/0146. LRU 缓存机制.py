'''
    运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
    实现 LRUCache 类：

    LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
    int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
    void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
     
    进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？

    示例：

    输入
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    输出
    [null, null, null, 1, null, -1, null, -1, 3, 4]

    解释
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // 缓存是 {1=1}
    lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
    lRUCache.get(1);    // 返回 1
    lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    lRUCache.get(2);    // 返回 -1 (未找到)
    lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    lRUCache.get(1);    // 返回 -1 (未找到)
    lRUCache.get(3);    // 返回 3
    lRUCache.get(4);    // 返回 4
     
    提示：

    1 <= capacity <= 3000
    0 <= key <= 3000
    0 <= value <= 104
    最多调用 3 * 104 次 get 和 put

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class LinkNode(object):
    def __init__(self, key = None, val = None, pre = None, nxt = None):
        self.key = key
        self.val = val
        self.pre = pre
        self.nxt = nxt
    
    # 删除第一个节点
    def remove_first(self):
        new_head = self.nxt
        if new_head is not None:
            new_head.pre = None
        del self
        return new_head
    
    # 删除中间节点
    def remove_mid(self):
        pre_node = self.pre
        nxt_node = self.nxt
        pre_node.nxt = nxt_node
        nxt_node.pre = pre_node
        del self

    # 在最后插入节点
    def insert_last(self, new_tail):
        self.nxt = new_tail
        new_tail.pre = self
        return new_tail

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.max_num = capacity
        self.cur_num = 0
        self.hashMap = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashMap:
            new_node = self.hashMap[key]
            self.update_node(new_node)
            return new_node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        new_node = LinkNode(key, value)
        # 更新key对应的val，同时放在链表最后
        if key in self.hashMap:
            self.update_node(new_node)
        else:
            if self.cur_num == 0:
                self.head = self.tail = new_node
                self.cur_num += 1
            # 哈希表没有满
            elif self.cur_num < self.max_num:
                self.cur_num += 1
                self.tail = self.tail.insert_last(new_node)
            # 哈希表已经满了
            else:
                del self.hashMap[self.head.key]
                if self.max_num == 1:
                    self.head = self.tail = new_node
                else:
                    self.head = self.head.remove_first()
                    self.tail = self.tail.insert_last(new_node)
            self.hashMap[key] = new_node
    
    def update_node(self, new_node):
        key = new_node.key
        if key == self.tail.key:
            self.tail.val = new_node.val
            self.hashMap[key].val = new_node.val
        elif key == self.head.key:
            self.head = self.head.remove_first()
            self.tail = self.tail.insert_last(new_node)
            self.hashMap[key] = new_node
        else:
            self.hashMap[key].remove_mid()
            self.tail = self.tail.insert_last(new_node)
            self.hashMap[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)