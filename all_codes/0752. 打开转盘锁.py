'''
    你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

    锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

    列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

    字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

    示例:

    输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
    输出：6
    解释：
    可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
    注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
    因为当拨动到 "0102" 时这个锁就会被锁定。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/open-the-lock
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        
        lock_visited = set(deadends)
        if (target in lock_visited) or ('0000' in lock_visited):
            return -1
        step = 0
        queue = ['0000']
        lock_visited.add('0000')
        
        # BFS
        while queue:
            # 遍历该层节点
            index = 0
            size = len(queue)
            while index < size:
                index += 1
                lock_str = queue.pop(0)
                
                # 判断是否结束
                if lock_str == target:
                    return step

                # 将下一层的节点加入队列
                for i in range(4):
                    # 第i个数字加一
                    next_str = lock_str[:i] + str((int(lock_str[i])+1)%10) + lock_str[i+1:]
                    if next_str not in lock_visited:
                        queue.append(next_str)
                        lock_visited.add(next_str)
                    # 第i个数字减一
                    next_str = lock_str[:i] + str((int(lock_str[i])-1)%10) + lock_str[i+1:]
                    if next_str not in lock_visited:
                        queue.append(next_str)
                        lock_visited.add(next_str)
            
            # 层数加一
            step += 1

        return -1