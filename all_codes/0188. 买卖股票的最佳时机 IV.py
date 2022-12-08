'''
    给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

    设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    示例 1：

    输入：k = 2, prices = [2,4,1]
    输出：2
    解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
    
    示例 2：

    输入：k = 2, prices = [3,2,6,5,0,3]
    输出：7
    解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
        随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

    提示：

    0 <= k <= 109
    0 <= prices.length <= 1000
    0 <= prices[i] <= 1000

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from sys import maxsize
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        '''
        状态描述 day：天数 k：可交易次数 hold：1 or 0，当前是否持有股票
        选择描述 买，卖，无操作
        dp[day][k][1] <- 无操作：dp[day-1][k][1]
                         买：dp[day-1][k+1][0]
        dp[day][k][0] <- 无操作：dp[day-1][k][0]
                         卖：dp[day-1][k][1] + price[day-1]
        '''
        # 定义第 day=-1的初始状态
        lenth = len(prices)
        k = min(k, lenth//2)
        if k <= 0:
            return 0
        dp = [[0 for i in range(k)], [(-maxsize - 1) for i in range(k)]]
        for i in range(len(prices)):
            j = k - 1
            while j >= 0:
                if j == k-1:
                    dp[0][j] = max(dp[0][j], dp[1][j] + prices[i])
                    dp[1][j] = max(dp[1][j], -prices[i])
                else:
                    dp[0][j] = max(dp[0][j], dp[1][j] + prices[i])
                    dp[1][j] = max(dp[1][j], dp[0][j+1]-prices[i])
                j -= 1
        
        return dp[0][0]