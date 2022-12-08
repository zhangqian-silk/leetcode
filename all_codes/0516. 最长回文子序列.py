'''
    给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

    示例 1:
    输入:

    "bbbab"
    输出:4
    一个可能的最长回文子序列为 "bbbb"。

    示例 2:
    输入:

    "cbbd"
    输出:2
    一个可能的最长回文子序列为 "bb"。

    提示：

    1 <= s.length <= 1000
    s 只包含小写英文字母

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        dp[i][j]表示 j 和 i 之间的最长回文子序列
        i >= j
        i == j, i == j+1 要单独判断
        s[i]==s[j]: dp[i][j] = dp[i-1][j+1] + 2
        s[i]!=s[j]: dp[i][j] = max(dp[i][j+1], dp[i-1][j])
        '''
        
        dp = []
        lenth = len(s)
        
        for i in range(lenth):
            dp.append([0 for _ in range(i+1)])
            j = i
            while j >= 0:
                if j == i:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    if j+1 == i:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i-1][j+1] + 2
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i-1][j])
                j -= 1
        return dp[lenth-1][lenth-1]