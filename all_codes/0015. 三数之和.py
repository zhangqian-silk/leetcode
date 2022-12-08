'''
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

    注意：答案中不可以包含重复的三元组。

    示例：

    给定数组 nums = [-1, 0, 1, 2, -1, -4]，

    满足要求的三元组集合为：
    [
    [-1, 0, 1],
    [-1, -1, 2]
    ]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/3sum
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        # n>=2
        def nSum(nums, n, target):
            
            numbers = nums[:]
            all_res = []
            if n == 2:
                left = 0
                right = len(numbers) - 1
                
                while left < right:
                    num_left = numbers[left]
                    num_right = numbers[right]
                    if num_left + num_right > target:
                        while (left < right) and (numbers[right] == num_right):
                            right -= 1
                    elif num_left + num_right < target:
                        while (left < right) and (numbers[left] == num_left):
                            left += 1
                    elif num_left + num_right == target:
                        all_res.append([num_left, num_right])
                        while (left < right) and (numbers[right] == num_right):
                            right -= 1
                        while (left < right) and (numbers[left] == num_left):
                            left += 1
                return all_res
            
            i = 0
            while numbers:
                num = numbers.pop(i)
                pre_ress = nSum(numbers, n - 1, target - num)
                if pre_ress:
                    res = [[num]+pre_res for pre_res in pre_ress]
                    all_res += res
                while numbers and (numbers[0] == num):
                    numbers.pop(0)
            return all_res
        return nSum(nums, 3, 0)


