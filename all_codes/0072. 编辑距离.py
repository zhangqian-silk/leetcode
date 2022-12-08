'''
    给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

    你可以对一个单词进行如下三种操作：

    插入一个字符
    删除一个字符
    替换一个字符

    示例 1：

    输入：word1 = "horse", word2 = "ros"
    输出：3
    解释：
    horse -> rorse (将 'h' 替换为 'r')
    rorse -> rose (删除 'r')
    rose -> ros (删除 'e')

    示例 2：

    输入：word1 = "intention", word2 = "execution"
    输出：5
    解释：
    intention -> inention (删除 't')
    inention -> enention (将 'i' 替换为 'e')
    enention -> exention (将 'n' 替换为 'x')
    exention -> exection (将 'n' 替换为 'c')
    exection -> execution (插入 'u')
     
    提示：

    0 <= word1.length, word2.length <= 500
    word1 和 word2 由小写英文字母组成

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/edit-distance
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        '''
        i 表示 word1 索引
        j 表示 word2 索引
        dp[i][j] 表示 word1 前i位和 word2 前j位相同所用步数
        dp[i][j] = dp[i-1][j] + 1   删除
                 = dp[i-1][j-1] + 1 替换
                 = dp[i][j-1] + 1   插入
        pre_dp 用来记录dp[i][j-1]的值
        因为dp[i][j]的值与dp[i-1][j-1]有关，所以状态压缩的情况下，
        需要更新完当前值时，再更新dp[i-1][j-1]
        '''
        lenth1, lenth2 = len(word1), len(word2)
        dp = [j for j in range(lenth2+1)]

        for i in range(1, lenth1+1):
            pre_dp_i_j = i
            for j in range(1, lenth2+1):
                if word1[i-1] == word2[j-1]:
                    dp_i_j = dp[j-1]
                    dp[j-1] = pre_dp_i_j
                    pre_dp_i_j = dp_i_j
                else:
                    dp_i_j = min(dp[j], dp[j-1], pre_dp_i_j) + 1
                    dp[j-1] = pre_dp_i_j
                    pre_dp_i_j = dp_i_j
            dp[lenth2] = pre_dp_i_j
            
        return dp[lenth2]