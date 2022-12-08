'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 区间为 [left,right)
        left_leftpart = 0
        right_rightpart = len(nums)
        if right_rightpart <= left_leftpart:
            return [-1, -1]
        
        # 二分查找，先找到一个等于target的索引下标
        while left_leftpart < right_rightpart:
            mid = (left_leftpart + right_rightpart) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                left_leftpart = mid + 1
            elif nums[mid] > target:
                right_rightpart = mid
        
        # 找边界
        if nums[mid] == target:
            right_leftpart = left_rightpart = mid
            
            # 左边界为left_leftpart
            while left_leftpart < right_leftpart:
                mid_leftpart = (left_leftpart + right_leftpart) // 2
                if nums[mid_leftpart] == target:
                    right_leftpart = mid_leftpart
                elif nums[mid_leftpart] < target:
                    left_leftpart = mid_leftpart + 1
            
            # 右边界为right_rightpart
            while left_rightpart < right_rightpart:
                mid_rightpart = (left_rightpart + right_rightpart) // 2
                if nums[mid_rightpart] == target:
                    left_rightpart = mid_rightpart + 1
                elif nums[mid_rightpart] > target:
                    right_rightpart = mid_rightpart
            # nums[left_rightpart] == target
            left_rightpart = left_rightpart - 1
        else:
            return [-1, -1]
        
        return [left_leftpart, left_rightpart]

