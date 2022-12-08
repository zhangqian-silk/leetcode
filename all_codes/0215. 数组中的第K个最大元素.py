'''
    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

    示例 1:

    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5

    示例 2:

    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4
    说明:

    你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from random import randint 
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # 对数组nums的[left,right]范围内进行一次分割，返回分界位置的索引
        def partition(nums, left, right):
            # 随机化标准值
            if left >= right:
                return left
            i = randint(left, right)
            key = nums[i]
            nums[i] = nums[left]
            nums[left] = key
            
            # 交换列表元素并找到分界位置
            while left < right:
                while left < right and nums[right] <= key:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] > key:
                    left += 1
                nums[right] = nums[left]
            nums[left] = key
            return left
        
        lenth = len(nums)
        index = partition(nums, 0, lenth - 1)
        
        # 控制查找的边界
        index_left = 0
        index_right = lenth - 1
        
        # 查找索引
        while index != k-1:
            if index > k-1:
                index_right = index
                index = partition(nums, index_left, index - 1)
            elif index < k-1:
                index_left = index
                index = partition(nums, index + 1, index_right)
        
        return nums[index]
                