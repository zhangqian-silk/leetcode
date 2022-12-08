'''
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

    示例 1：

    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。

    示例 2：

    输入: "cbbd"
    输出: "bb"

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/longest-palindromic-substring
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lenth = len(s)
        if lenth == 0:
            return ""
        elif lenth == 1:
            return s
        dp = []
        res = [0, 0]
        # i <= j 矩阵取下三角矩阵，j表示行，i表示列
        for j in range(lenth):
            dp.append([])
            for i in range(j+1):
                if s[j] == s[i]:
                    if j - i >= 2:
                        if dp[j-1][i+1] == 'T':
                            dp[j].append('T')
                            if j - i > res[1] - res[0]:
                                res = [i, j]
                        else:
                            dp[j].append('F')
                    else:
                        dp[j].append('T')
                        if j - i > res[1] - res[0]:
                            res = [i, j]
                else:
                    dp[j].append('F')
        return s[res[0]:res[1]+1]


        
                    
                