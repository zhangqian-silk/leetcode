package main

import "slices"

/*
	给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

	示例 1：
		输入：nums = [1,1,2]
		输出：
		[[1,1,2],
		[1,2,1],
		[2,1,1]]

	示例 2：
		输入：nums = [1,2,3]
		输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

	提示：
		1 <= nums.length <= 8
		-10 <= nums[i] <= 10

	link: https://leetcode.cn/problems/permutations-ii/description/
*/

func PermuteUnique(nums []int) [][]int {
	visited := make(map[int]struct{}, 0)
	slices.Sort(nums)
	var res [][]int

	// dfs + 回溯，枚举出所有排列情况，并剪枝掉重复的序列
	var dfs func(nums []int)
	dfs = func(path []int) {
		if len(path) == len(nums) {
			// 注意切片是引用类型，这里需要一次 copy 操作
			finalPath := make([]int, len(path))
			copy(finalPath, path)
			res = append(res, finalPath)
			return
		}
		last := -1
		for i := range len(nums) {
			if _, ok := visited[i]; ok {
				continue
			}
			if last >= 0 && nums[i] == nums[last] {
				// 如果当次选择与上次选择的值一样，则排列出的序列一定重复
				continue
			}
			visited[i] = struct{}{}
			dfs(append(path, nums[i]))
			delete(visited, i)
			last = i
		}
	}
	dfs(make([]int, 0, len(nums)))
	return res
}
