'''
    给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

    注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

    示例 1：

    输入：s = "ADOBECODEBANC", t = "ABC"
    输出："BANC"

    示例 2：

    输入：s = "a", t = "a"
    输出："a"

    提示：

    1 <= s.length, t.length <= 105
    s 和 t 由英文字母组成
     
    进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/minimum-window-substring
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        need = {}
        have = {}
        
        for i in range(len(t)):
            if t[i] in need:
                need[t[i]] += 1
            else:
                need[t[i]] = 1
                have[t[i]] = 0
        need_size = len(need)
        have_size = begin = left = right = 0
        lenth = end = len(s)
        
        # 扩大窗口
        while right < lenth:
            c = s[right]
            if c in need:
                have[c] += 1
                if have[c] == need[c]:
                    have_size += 1
            
            # 缩小窗口
            while have_size == need_size:
                if right - left < end - begin:
                    begin, end = left, right
                c = s[left]
                if c in need:
                    have[c] -= 1
                    if have[c] < need[c]:
                        have_size -= 1
                left += 1
            
            right += 1
        
        if end == lenth:
            end = begin
        else:
            end += 1
        return s[begin:end]
            