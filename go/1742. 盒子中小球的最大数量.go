package main

/*
	你在一家生产小球的玩具厂工作，有 n 个小球，编号从 lowLimit 开始，到 highLimit 结束（包括 lowLimit 和 highLimit ，即 n == highLimit - lowLimit + 1）。另有无限数量的盒子，编号从 1 到 infinity 。

	你的工作是将每个小球放入盒子中，其中盒子的编号应当等于小球编号上每位数字的和。例如，编号 321 的小球应当放入编号 3 + 2 + 1 = 6 的盒子，而编号 10 的小球应当放入编号 1 + 0 = 1 的盒子。

	给你两个整数 lowLimit 和 highLimit ，返回放有最多小球的盒子中的小球数量。如果有多个盒子都满足放有最多小球，只需返回其中任一盒子的小球数量。

	示例 1：

		输入：lowLimit = 1, highLimit = 10
		输出：2
		解释：
		盒子编号：1 2 3 4 5 6 7 8 9 10 11 ...
		小球数量：2 1 1 1 1 1 1 1 1 0  0  ...
		编号 1 的盒子放有最多小球，小球数量为 2 。

	示例 2：

		输入：lowLimit = 5, highLimit = 15
		输出：2
		解释：
		盒子编号：1 2 3 4 5 6 7 8 9 10 11 ...
		小球数量：1 1 1 1 2 2 1 1 1 0  0  ...
		编号 5 和 6 的盒子放有最多小球，每个盒子中的小球数量都是 2 。

	示例 3：

		输入：lowLimit = 19, highLimit = 28
		输出：2
		解释：
		盒子编号：1 2 3 4 5 6 7 8 9 10 11 12 ...
		小球数量：0 1 1 1 1 1 1 1 1 2  0  0  ...
		编号 10 的盒子放有最多小球，小球数量为 2 。


	提示：

		1 <= lowLimit <= highLimit <= 10^5

	link: https://leetcode.cn/problems/maximum-number-of-balls-in-a-box/description/
*/

func CountBalls_1742(lowLimit int, highLimit int) int {
	var res int
	// hightLimit 上限为 10^5，所以 key 最大为 99999 各位数字的合
	// 注意 key 为连续的自然数，所以用 slice 而不是 map
	ballMap := make([]int, 46)
	for i := lowLimit; i <= highLimit; i++ {
		var totalNum int
		for num := i; num > 0; num /= 10 {
			totalNum += num % 10
		}
		ballMap[totalNum] += 1
		res = max(res, ballMap[totalNum])
	}
	return res
}
