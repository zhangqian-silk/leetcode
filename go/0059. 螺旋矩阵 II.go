package main

import "fmt"

/*
	给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

	示例 1：
		输入：n = 3
		输出：[[1,2,3],[8,9,4],[7,6,5]]

	示例 2：
		输入：n = 1
		输出：[[1]]

	提示：
		1 <= n <= 20
*/

func generateMatrix(n int) [][]int {
	res := make([][]int, n)
	for i := range n {
		res[i] = make([]int, n)
	}

	// direction 表示每次前进的方向
	direction := 0
	// level 表示已经铺满的层级，会决定最大前进长度
	level := 0
	// i、j 表示当前坐标
	i := 0
	j := 0
	for e := range n * n {
		fmt.Println(e+1, i, j, direction)
		res[i][j] = e + 1

		if direction == 0 {
			// 向右前进
			if j < n-level-1 {
				j++
			} else {
				direction += 1
				i++
			}
		} else if direction == 1 {
			// 向下前进
			if i < n-level-1 {
				i++
			} else {
				direction += 1
				j--
			}
		} else if direction == 2 {
			// 向左前进
			if j > level {
				j--
			} else {
				direction += 1
				i--
			}
		} else if direction == 3 {
			// 向上前进, i = level-1 时，会回到这一圈的起点
			// 所以 i 不能小于 level
			if i > level+1 {
				i--
			} else {
				direction = 0
				j++
				level++
			}
		}
	}

	return res
}
