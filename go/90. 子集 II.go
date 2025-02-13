package main

import (
	"slices"
)

/*
	给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

	解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

	示例 1：

		输入：nums = [1,2,2]
		输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

	示例 2：

		输入：nums = [0]
		输出：[[],[0]]

	提示：

		1 <= nums.length <= 10
		-10 <= nums[i] <= 10

	link: https://leetcode.cn/problems/subsets-ii/description/
*/

func SubsetsWithDup(nums []int) [][]int {
	/*
		用二进制数据表示数组中各位数的选择情况，即 0 - 11...11 (长度为 nums.length)

		针对于重复元素，先将数组排序，然后判断重复场景并移除：
		- 以 1 2 2 2 3 为例，则 01000、00100、00010 重复，01100、01010、00110 重复，等等
		- 此时，仅保留连续选择的特殊情况，即保留 01000、01100、01110（第一位与第五位随意）
		- 在这种情况下，先通过与 01110 做与运算，判断是否选中了重复元素
		- 然后再判断这部分的选择情况，是否连续
	*/
	slices.Sort(nums)
	length := len(nums)

	// 计算出所有重复的特殊情况
	checkMap := make(map[int]int, 0)
	for i := 0; i < length; {
		// j 是第一个不等于 i 的索引
		j := i + 1
		for j < length && nums[i] == nums[j] {
			j++
		}
		if j-i == 1 {
			i = j
			continue
		}

		checkMap[(1<<(j-i)-1)<<i] = i
		i = j
	}

	maxValue := 1 << length
	res := make([][]int, 0, maxValue)
	for i := range maxValue {
		// 如果 i 中包含 removeList 中的特殊情况，直接丢弃
		flag := false
		for k, index := range checkMap {
			checkRes := i & k
			if checkRes > 0 {
				// 包含重复元素时，右移循环判断为 1 的位置是否连续
				newI := checkRes >> index
				for newI > 0 {
					if newI&1 == 0 {
						// 异常情况，例如 1010，需要移除
						flag = true
						break
					}
					newI = newI >> 1
				}
			}
			if flag {
				break
			}
		}

		if flag {
			continue
		}

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
