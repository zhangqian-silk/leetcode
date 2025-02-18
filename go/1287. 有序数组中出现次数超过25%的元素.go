package main

/*
	给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。

	请你找到并返回这个整数

	示例：

		输入：arr = [1,2,2,6,6,6,6,7,10]
		输出：6

	提示：

		1 <= arr.length <= 10^4
		0 <= arr[i] <= 10^5

	link: https://leetcode.cn/problems/element-appearing-more-than-25-in-sorted-array/description/
*/

func findSpecialInteger(arr []int) int {
	length := len(arr) / 4
	var i int
	for {
		// 按照题意，一定存在，所以不判断边界
		// if i + length >= len(arr) { return 0 }

		// 因为数组本身是递增的，所以直接判断满足长度要求时
		// 对应位置的元素是否不变
		if arr[i+length] == arr[i] {
			return arr[i]
		}

		// 不满足条件时，将 i 递增
		i++
	}
}
