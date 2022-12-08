'''
    给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

    你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

    返回获得利润的最大值。

    注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

    示例 1:

    输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
    输出: 8
    解释: 能够达到的最大利润:  
    在此处买入 prices[0] = 1
    在此处卖出 prices[3] = 8
    在此处买入 prices[4] = 4
    在此处卖出 prices[5] = 9
    总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
    注意:

    0 < prices.length <= 50000.
    0 < prices[i] < 50000.
    0 <= fee < 50000.

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from sys import maxsize
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        '''
        状态描述 day：天数 k：可交易次数 hold：1 or 0，当前是否持有股票
        选择描述 买，卖，无操作
        dp[day][k][1] <- 无操作：dp[day-1][k][1]
                         买：dp[day-1][k+1][0] - prices[day-1]
        dp[day][k][0] <- 无操作：dp[day-1][k][0]
                         卖：dp[day-1][k][1] + price[day-1]
        '''
        # 定义第 day=-1的初始状态
        dp_i_0 = 0
        dp_i_1 = -maxsize - 1
        for i in range(len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)
            dp_i_1 = max(dp_i_1, temp - prices[i])

        return dp_i_0