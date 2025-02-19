package main

/*
	给定一个 m x n 的整数数组 grid。一个机器人初始位于 左上角（即 grid[0][0]）。机器人尝试移动到 右下角（即 grid[m - 1][n - 1]）。机器人每次只能向下或者向右移动一步。

	网格中的障碍物和空位置分别用 1 和 0 来表示。机器人的移动路径中不能包含 任何 有障碍物的方格。

	返回机器人能够到达右下角的不同路径数量。

	测试用例保证答案小于等于 2 * 109。

	示例 1：

		输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
		输出：2
		解释：3x3 网格的正中间有一个障碍物。
		从左上角到右下角一共有 2 条不同的路径：
		1. 向右 -> 向右 -> 向下 -> 向下
		2. 向下 -> 向下 -> 向右 -> 向右

	示例 2：

		输入：obstacleGrid = [[0,1],[0,0]]
		输出：1

	提示：

		m == obstacleGrid.length
		n == obstacleGrid[i].length
		1 <= m, n <= 100
		obstacleGrid[i][j] 为 0 或 1

	link: https://leetcode.cn/problems/unique-paths-ii/description/
*/

func UniquePathsWithObstacles_63(obstacleGrid [][]int) int {
	/*
		因为只能向下或者向右移动，所以有：
			dp[i][j] = dp[i][j-1] + dp[i-1][j]

		可发现 dp[i][j] 仅与当前行的前一列元素和上一行的当前列的元素有关，
		故可以只使用一维 dp：
			index 之前为当前行元素
			indx 本身以及之后为上一行元素
	*/

	m := len(obstacleGrid)
	n := len(obstacleGrid[0])
	dp := make([]int, n)
	for i := range m {
		for j := range n {
			if obstacleGrid[i][j] == 1 {
				dp[j] = 0
			} else if j == 0 {
				if i == 0 {
					dp[j] = 1
				}
			} else {
				dp[j] = dp[j] + dp[j-1]
			}
		}
	}
	return dp[n-1]
}
