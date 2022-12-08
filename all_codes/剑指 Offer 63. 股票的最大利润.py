'''
    假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

    示例 1:

    输入: [7,1,5,3,6,4]
    输出: 5
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
        注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

    示例 2:

    输入: [7,6,4,3,1]
    输出: 0
    解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
     
    限制：

    0 <= 数组长度 <= 10^5
     
    注意：本题与主站 121 题相同：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof
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
        dp[day][k][1] <- 无操作：dp[day-1][k][1]
                         买：dp[day-1][k+1][0] - price[day-1]
        dp[day][k][0] <- 无操作：dp[day-1][k][0]
                         卖：dp[day-1][k][1] + price[day-1]
        '''
        # 定义第 day=-1的初始状态
        dp_i_0 = 0
        dp_i_1 = -maxsize - 1
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        
        return dp_i_0