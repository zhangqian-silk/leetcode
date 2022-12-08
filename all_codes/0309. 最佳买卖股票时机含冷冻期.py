'''
    给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
    示例:

    输入: [1,2,3,0,2]
    输出: 3 
    解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from sys import maxsize
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        状态描述 day：天数 k：可交易次数 hold：1 or 0，当前是否持有股票
        选择描述 买，卖，无操作
        交易有冷冻期，买入时要注意天数状态的变化
        dp[day][k][1] <- 无操作：dp[day-1][k][1]
                         买：dp[day-2][k+1][0] - prices[day-1]
        dp[day][k][0] <- 无操作：dp[day-1][k][0]
                         卖：dp[day-1][k][1] + price[day-1]
        '''
        # 定义第 day=-1的初始状态
        pre_dp_i_0 = dp_i_0 = 0
        dp_i_1 = -maxsize - 1
        for i in range(len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, pre_dp_i_0 - prices[i])
            pre_dp_i_0 = temp

        return dp_i_0