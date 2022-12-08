'''
    给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

    换句话说，第一个字符串的排列之一是第二个字符串的子串。

    示例1:

    输入: s1 = "ab" s2 = "eidbaooo"
    输出: True
    解释: s2 包含 s1 的排列之一 ("ba").

    示例2:

    输入: s1= "ab" s2 = "eidboaoo"
    输出: False

    注意：

    输入的字符串只包含小写字母
    两个字符串的长度都在 [1, 10,000] 之间

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/permutation-in-string
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        need = {}
        have = {}
        for i in range(len(s1)):
            if s1[i] in need:
                need[s1[i]] += 1
            else:
                need[s1[i]] = 1
        need_size = len(need)
        have_size = right = 0
        left = -1
        lenth = len(s2)
        
        # 窗口内字符都属于s1，窗口大小为[left+1,right]
        while right < lenth:
            if s2[right] in need:
                if s2[right] in have:
                    have[s2[right]] += 1
                    # 窗口缩小
                    while have[s2[right]] > need[s2[right]]:
                        left += 1
                        if have[s2[left]] == need[s2[left]] or s2[left] == s2[right]:
                            have_size -= 1
                        have[s2[left]] -= 1
                else:
                    have[s2[right]] = 1
                if have[s2[right]] == need[s2[right]]:
                        have_size += 1
            else:
                left = right
                have.clear()
                have_size = 0

            if have_size == need_size:
                return True
            
            right += 1
        return False

                
