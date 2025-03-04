package main

/*
	给你一个由小写字母组成的字符串 s，和一个整数 k。

	请你按下面的要求分割字符串：

	首先，你可以将 s 中的部分字符修改为其他的小写英文字母。
	接着，你需要把 s 分割成 k 个非空且不相交的子串，并且每个子串都是回文串。
	请返回以这种方式分割字符串所需修改的最少字符数。

	示例 1：

		输入：s = "abc", k = 2
		输出：1
		解释：你可以把字符串分割成 "ab" 和 "c"，并修改 "ab" 中的 1 个字符，将它变成回文串。

	示例 2：

		输入：s = "aabbc", k = 3
		输出：0
		解释：你可以把字符串分割成 "aa"、"bb" 和 "c"，它们都是回文串。

	示例 3：

		输入：s = "leetcode", k = 8
		输出：0

	提示：

		1 <= k <= s.length <= 100
		s 中只含有小写英文字母。

	link: https://leetcode.cn/problems/palindrome-partitioning-iii/description/
*/

func cost_1278(s string, i, j int) int {
	if i > j {
		return len(s)
	}

	var res int
	for i <= j {
		if s[i] != s[j] {
			res++
		}
		i++
		j--
	}
	return res
}

func PalindromePartition_1278(s string, k int) int {
	// dp[i][j] 表示前 j 个字符，分割成 i 个回文串最小改动字符数
	// 如果当前字符需要新进行分割，dp[i][j] = dp[i-1][j-1]
	// 如果当前字符不重新进行分割，则需要与其他字符进行合并，并判断消耗大小
	// dp[i][j] = min(dp[i-1][n-1]+cost(n,j)) (i-1 < n < j)
	// i 只与 i-1 相关，所以只用两个数组即可
	dp := make([]int, len(s))
	lastDp := make([]int, len(s))

	for i := range len(s) {
		// 初始化分给成 1 个回文串时的最小改动字符数
		lastDp[i] = cost_1278(s, 0, i)
	}

	// lastDp 已经初始化为拆分为一个字符串时的消耗
	// 直接从 i = 2 开始遍历
	for i := 2; i <= k; i++ {
		// j 小于 i-1 时，无法遍历
		// j 等于 i-1 时，全部拆分为单字符，无需遍历
		dp[i-1] = 0
		for j := i; j < len(s); j++ {
			minCost := lastDp[j-1]
			// n 最小索引为 n-1，需要满足 n 之前至少有 i-1 个字符
			for n := i - 1; n < j; n++ {
				minCost = min(minCost, lastDp[n-1]+cost_1278(s, n, j))
			}
			dp[j] = minCost
		}
		// 更新 lastDP 为当前切片，旧有数据可以丢弃
		lastDp, dp = dp, lastDp
	}

	return lastDp[len(s)-1]
}
