'''
    有一堆石头，每块石头的重量都是正整数。

    每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

    如果 x == y，那么两块石头都会被完全粉碎；
    如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
    最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。

    示例：

    输入：[2,7,4,1,8,1]
    输出：1
    解释：
    组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
    组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
    组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
    组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。

    提示：

    1 <= stones.length <= 30
    1 <= stones[i] <= 1000

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/last-stone-weight-ii
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) is 0:
            return 0
        stones.sort(reverse = True)
        lenth = len(stones)
        sums = sum(stones)
        sums_2 = sums // 2
        dp = []
        dp.append([0 for i in range(lenth)])
        for i in range(1, sums_2+1):
            dp.append([])
            dp[i].append(0)
            for j in range(1, lenth+1):
                dp[i].append(0)
                if stones[j-1] <= i:
                    dp[i][j] = max(dp[i][j-1], dp[i-stones[j-1]][j-1]+stones[j-1])
                else:
                    dp[i][j] = dp[i][j-1]
        return sums - 2*dp[sums_2][lenth]