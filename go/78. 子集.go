package main

/*
	给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

	解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

	示例 1：

		输入：nums = [1,2,3]
		输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

	示例 2：

		输入：nums = [0]
		输出：[[],[0]]

	提示：

		1 <= nums.length <= 10
		-10 <= nums[i] <= 10
		nums 中的所有元素 互不相同

	link: https://leetcode.cn/problems/subsets/description/
*/

func Subsets_78(nums []int) [][]int {
	// 用二进制数据表示数组中各位数的选择情况，即 0 - 11...11 (长度为 nums.length)
	length := len(nums)
	maxValue := 1 << length
	res := make([][]int, 0, maxValue)
	for i := range maxValue {
		localRes := make([]int, 0, length)
		for j := range length {
			if i&(1<<j) > 0 {
				localRes = append(localRes, nums[j])
			}
		}
		res = append(res, localRes)
	}

	return res
}
