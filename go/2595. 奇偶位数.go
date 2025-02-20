package main

/*
	给你一个 正 整数 n 。

	用 even 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的偶数下标的个数。

	用 odd 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的奇数下标的个数。

	请注意，在数字的二进制表示中，位下标的顺序 从右到左。

	返回整数数组 answer ，其中 answer = [even, odd] 。


	示例 1：

		输入：n = 50

		输出：[1,2]

		解释：

		50 的二进制表示是 110010。

		在下标 1，4，5 对应的值为 1。

	示例 2：

		输入：n = 2

		输出：[0,1]

		解释：

		2 的二进制表示是 10。

		只有下标 1 对应的值为 1。

	提示：

		1 <= n <= 1000

	link: https://leetcode.cn/problems/number-of-even-and-odd-bits/description/
*/

func EvenOddBit_2595(n int) []int {
	// 通过右移，循环判断最后一位是否为 1
	// 用 flag 表示位置的奇偶
	// 每次右移时，将 flag 最后一位取分
	res := []int{0, 0}
	var flag int
	for n > 0 {
		res[flag] += n & 1
		n = n >> 1
		flag ^= 1
	}
	return res
}
