package main

/*
	给你一个下标从 0 开始的 二进制 字符串 floor ，它表示地板上砖块的颜色。

	floor[i] = '0' 表示地板上第 i 块砖块的颜色是 黑色 。
	floor[i] = '1' 表示地板上第 i 块砖块的颜色是 白色 。
	同时给你 numCarpets 和 carpetLen 。你有 numCarpets 条 黑色 的地毯，每一条 黑色 的地毯长度都为 carpetLen 块砖块。请你使用这些地毯去覆盖砖块，使得未被覆盖的剩余 白色 砖块的数目 最小 。地毯相互之间可以覆盖。

	请你返回没被覆盖的白色砖块的 最少 数目。

	示例 1：

		输入：floor = "10110101", numCarpets = 2, carpetLen = 2
		输出：2
		解释：
		上图展示了剩余 2 块白色砖块的方案。
		没有其他方案可以使未被覆盖的白色砖块少于 2 块。

	示例 2：

		输入：floor = "11111", numCarpets = 2, carpetLen = 3
		输出：0
		解释：
		上图展示了所有白色砖块都被覆盖的一种方案。
		注意，地毯相互之间可以覆盖。

	提示：

		1 <= carpetLen <= floor.length <= 1000
		floor[i] 要么是 '0' ，要么是 '1' 。
		1 <= numCarpets <= 1000

	link: https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/description/
*/

func minimumWhiteTiles(floor string, numCarpets int, carpetLen int) int {
	/*
		dp[i][j] 表示用 i 个地毯覆盖前 j 个地板时，剩余白色地块的最小数目

		当 i = 0 时，dp[i][j] 为白色地板数量，
			- 即 dp[i][j] = dp[i][j-1] + floor[j]

		当 i * carpetLen >= j 时，地毯可以全覆盖，dp[i][j] = 0

		当 i * carpetLen < j 时：
			- 如果第 i 块地毯，覆盖第 j 个地板，则需要从 j-carpetLen+1 开始覆盖，所以此时与 i-1 块地毯，覆盖前 j-carpetLen 个地板的情况相等
				- 即 dp[i][j] = dp[i-1][j-carpetLen]
			- 如果第 i 块地毯，不覆盖第 j 个位置，则将 dp[i][j-1] 的结果，加上第 j 个位置的地板颜色即可
		  		- 即 dp[i][j] = dp[i][j-1] + floor[j]

		从推导来看，对于 i，只取 i-1，故采用一维 dp 即可
	*/

	dp := make([]int, len(floor))
	lastDp := make([]int, len(floor))

	// i 的枚举范围为 0 ~ numCarpets
	for i := range numCarpets + 1 {
		for j, value := range floor {
			if i == 0 {
				if j == 0 {
					dp[j] = int(value) - int('0')
				} else {
					dp[j] = dp[j-1] + int(value) - int('0')
				}
				continue
			}

			// j 从 0 开始枚举，但是地板长度为 j+1
			if i*carpetLen >= j+1 {
				dp[j] = 0
				continue
			}

			dp[j] = min(lastDp[j-carpetLen], dp[j-1]+int(value)-int('0'))
		}

		lastDp, dp = dp, lastDp
	}
	return lastDp[len(floor)-1]
}
