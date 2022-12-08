'''
    给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

    如果剩余字符少于 k 个，则将剩余字符全部反转。
    如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

    示例:

    输入: s = "abcdefg", k = 2
    输出: "bacdfeg"

    提示：

    该字符串只包含小写英文字母。
    给定字符串的长度和 k 在 [1, 10000] 范围内。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/reverse-string-ii
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        start_2k = 0
        lenth = len(s)
        right = 0
        left = 0
        list_str = list(s)
        # start_2k记录每个2k的位置
        while start_2k < lenth:
            left = start_2k
            right = min(left+k-1, lenth-1)
            # 反转列表
            while left < right:
                num = s[left]
                list_str[left] = list_str[right]
                list_str[right] = num
                left += 1
                right -= 1
            start_2k += 2*k 
        
        return ''.join(list_str)
