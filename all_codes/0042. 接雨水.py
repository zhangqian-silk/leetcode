'''
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

    示例 1：

    输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出：6
    解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

    示例 2：

    输入：height = [4,2,0,3,2,5]
    输出：9

    提示：

    n == height.length
    0 <= n <= 3 * 104
    0 <= height[i] <= 105

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/trapping-rain-water
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        lenth = len(height)
        if lenth <= 2:  
            return 0
        left = 0
        right = lenth - 1
        
        # left_max和right_max分别表示从左侧、右侧遍历得到的局部最大值
        left_max = height[left]
        right_max = height[right]
        res = 0
        while left <= right:
            # 每个点的容量，取决于左右两侧边界的较小值
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                res += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return res