package main

import "slices"

/*
	在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有 n 个空的篮子，第 i 个篮子的位置在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。

	已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。

	给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。

	示例 1：

		输入：position = [1,2,3,4,7], m = 3
		输出：3
		解释：将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。

	示例 2：

		输入：position = [5,4,3,2,1,1000000000], m = 2
		输出：999999999
		解释：我们使用位于 1 和 1000000000 的篮子时最小磁力最大。

	提示：

		n == position.length
		2 <= n <= 10^5
		1 <= position[i] <= 10^9
		所有 position 中的整数 互不相同 。
		2 <= m <= position.length

	link: https://leetcode.cn/problems/magnetic-force-between-two-balls/description/
*/

func maxDistance(position []int, m int) int {
	// 先将 position 排序，然后计算每两个位置间的磁力
	slices.Sort(position)
	nums := make([]int, len(position)-1)
	for i := 0; i < len(nums); i++ {
		nums[i] = position[i+1] - position[i]
	}

	// 当放置 m 个球时，最后会产生 m-1 个磁力
	// 对于最小磁力 res，将 nums 中的相邻元素
	// 进行合并，直至大于 res 的磁力数量为 m-1
	left := 0
	right := position[len(position)-1] - position[0]
	res := (left + right) / 2

	for left <= right {
		n := 0
		curValue := 0
		for _, num := range nums {
			curValue += num
			// 判断合并后的磁力，是否大于等于 res
			if curValue >= res {
				n += 1
				curValue = 0
			}
		}

		if n < m-1 {
			// res 过大，满足条件的剩余磁力数量过小
			right = res - 1
		} else {
			// 尝试继续将 res 增大
			left = res + 1
		}
		res = (left + right) / 2
	}

	return res
}
