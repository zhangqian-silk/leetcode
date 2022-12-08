'''
    给定一个 没有重复 数字的序列，返回其所有可能的全排列。

    示例:

    输入: [1,2,3]
    输出:
    [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
    ]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/permutations
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 逐个交换列表里的元素实现全排列
        def func(index = 0):
            if index == n:
                res.append(nums[:])
            else:
                for i in range(index, n):
                    nums[index], nums[i] = nums[i], nums[index]
                    func(index+1)
                    nums[index], nums[i] = nums[i], nums[index]
        
        n = len(nums)
        res = []
        func()
        return res

    