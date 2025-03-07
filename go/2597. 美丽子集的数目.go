package main

import "slices"

func BeautifulSubsets_2597(nums []int, k int) int {
	// 排序
	slices.Sort(nums)

	// 按照 mod k 进行分组
	modMap := make(map[int][]int)
	for _, num := range nums {
		modMap[num%k] = append(modMap[num%k], num)
	}

	// 单独处理每个组内元素，使其相差不为 k 即可
	// 最后将各个组的结果相乘
	res := 1
	for _, newNums := range modMap {
		// 计算前 n 个元素，有多少种方案(假设无重复元素)
		// - 不选 n 时，数量不变，dp[n] = dp[n-1]
		// - 选 n 时
		// 		- 如果 nums[n]-nums[n-1] = k，则出现冲突，
		// 		  此时有 dp[n] = dp[n-2]
		// 		- 如果 nums[n]-nums[n-1] != k，即没有冲突
		//    	  此时有 dp[n] = dp[n-1]
		//
		// 直接保存前两个结果即可
		// 对于元素重复的场景，额外乘以对应的子集数量，即 2^cnt，
		var curRes, lastRes, lastLastRes int
		for i := 0; i < len(newNums); i++ {
			// 统计当前元素数量
			curCnt := 1
			curNum := newNums[i]
			if i < len(newNums)-1 && newNums[i+1] == curNum {
				i++
				curCnt++
			}
			if curRes == 0 {
				// 第一个元素，直接初始化相关参数
				lastRes = 1 << curCnt
				curRes = 1 << curCnt
				lastLastRes = 1
				continue
			}

			if curNum-newNums[i-curCnt] != k {
				// curNum 可选可不选，直接乘以子集数量
				curRes = (1 << curCnt) * lastRes
			} else {
				// curNum 与 lastNum 冲突时
				//   - 要么不选，数量与 lastRes 相等
				//   - 要么必须选一个，此时子集数量为 2^cnt - 1，且不能选 lastNum，
				//     即乘以 lastLastRes
				curRes = lastRes + (1<<(curCnt)-1)*lastLastRes
			}
			lastLastRes = lastRes
			lastRes = curRes
		}
		res *= curRes
	}

	// 去除全空子集
	return res - 1
}
