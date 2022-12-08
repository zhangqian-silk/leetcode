'''
    给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
    对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

    返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

    示例：

    输入：nums: [1, 1, 1, 1, 1], S: 3
    输出：5
    解释：

    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3

    一共有5种方法让最终目标和为3。
     
    提示：

    数组非空，且长度不会超过 20 。
    初始的数组的和不会超过 1000 。
    保证返回的最终结果能被 32 位整数存下。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/target-sum
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # num_a - num_b = S
        # num_a + num_b = sum
        # num_a = s + sum // 2
        nums_sum = sum(nums)
        if nums_sum < S:
            return 0
        elif (nums_sum + S) % 2 == 1:
            return 0
        else:
            targrt = (nums_sum + S) // 2
        # i 表示前i个数字，j 目标大小，dp[i][j] 表示方法数量
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
        # 二维dp表中，从上到下，从右到左遍历
        lenth = len(nums)
        res = [0 for j in range(targrt+1)]
        res[0] = 1
        for i in range(1, lenth+1):
            j = targrt
            while j >= 0:
                if j-nums[i-1] >= 0:
                    res[j] += res[j-nums[i-1]]
                j -= 1
        return res[targrt]