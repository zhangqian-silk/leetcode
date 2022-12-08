'''
    给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

    注意:

    每个数组中的元素不会超过 100
    数组的大小不会超过 200
    
    示例 1:

    输入: [1, 5, 11, 5]

    输出: true

    解释: 数组可以分割成 [1, 5, 5] 和 [11].

    示例 2:

    输入: [1, 2, 3, 5]

    输出: false

    解释: 数组不能分割成两个元素和相等的子集.

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        i 表示数组元素，j 表示当前的目标大小
        dp[i][j] = max(选 i:dp[i-1][j-nums[i]] + nums[i]
                       不选:dp[i-1][j])
        '''
        lenth = len(nums)
        if lenth == 0:
            return True
        sums = sum(nums)
        if sums % 2 == 1:
            return False
        else:
            sums = sums // 2
        res = [0 for _ in range(sums+1)]
        for i in range(1, lenth+1):
            j = sums
            while j >= 0:
                if j - nums[i-1] >= 0:
                    dp = max(res[j-nums[i-1]]+nums[i-1], res[j])
                    res[j] = dp
                j -= 1
        return res[sums] == sums