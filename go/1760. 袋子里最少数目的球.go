package main

/*
	给你一个整数数组 nums ，其中 nums[i] 表示第 i 个袋子里球的数目。同时给你一个整数 maxOperations 。

	你可以进行如下操作至多 maxOperations 次：

	选择任意一个袋子，并将袋子里的球分到 2 个新的袋子中，每个袋子里都有 正整数 个球。
	比方说，一个袋子里有 5 个球，你可以把它们分到两个新袋子里，分别有 1 个和 4 个球，或者分别有 2 个和 3 个球。
	你的开销是单个袋子里球数目的 最大值 ，你想要 最小化 开销。

	请你返回进行上述操作后的最小开销。

	示例 1：

		输入：nums = [9], maxOperations = 2
		输出：3
		解释：
		- 将装有 9 个球的袋子分成装有 6 个和 3 个球的袋子。[9] -> [6,3] 。
		- 将装有 6 个球的袋子分成装有 3 个和 3 个球的袋子。[6,3] -> [3,3,3] 。
		装有最多球的袋子里装有 3 个球，所以开销为 3 并返回 3 。

	示例 2：

		输入：nums = [2,4,8,2], maxOperations = 4
		输出：2
		解释：
		- 将装有 8 个球的袋子分成装有 4 个和 4 个球的袋子。[2,4,8,2] -> [2,4,4,4,2] 。
		- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,4,4,4,2] -> [2,2,2,4,4,2] 。
		- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,4,4,2] -> [2,2,2,2,2,4,2] 。
		- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2] 。
		装有最多球的袋子里装有 2 个球，所以开销为 2 并返回 2 。

	示例 3：

		输入：nums = [7,17], maxOperations = 2
		输出：7

	提示：

		1 <= nums.length <= 10^5
		1 <= maxOperations, nums[i] <= 10^9

	link: https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag/description/
*/

func MinimumSize_1760(nums []int, maxOperations int) int {
	left := 0
	right := 1
	cur := 1
	flag := false
	for {
		op := 0
		for _, num := range nums {
			// 计算按照 cur 来分割时，所需最大操作
			if num > cur {
				// 将一个物品按照最大为 cur 进行分割
				op += (num - 1) / cur
				if op > maxOperations {
					break
				}
			}
		}

		if op > maxOperations {
			// cur 过小，需要的操作过多
			left = cur
			if right == cur {
				// right 和 cur 同时按照 2 倍进行增长，确定上界
				right *= 2
				cur = right
			} else {
				// 上界一定小于等于 right，此时 cur 取中间值，向上取整
				cur = (left + right + 1) / 2
			}
		} else {
			// cur 可以减小，取中间值，向下取整
			if flag && cur == right {
				// cur == right 有两种情况，通过 flag 进行区分
				// 第一种是翻倍增长时，cur 与 right 同步增长，所以到达上界首次减小时，cur 一定等于 right
				// 第二种是多次迭代后，right 与 left 差值小于等于 1，到达临界条件，right 为满足 op 的最小值
				return cur
			}
			flag = true
			right = cur
			cur = (left + right) / 2
		}
		if cur <= 0 {
			return 1
		}
	}
}
