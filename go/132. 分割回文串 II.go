package main

/*
	给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。

	返回符合要求的 最少分割次数 。

	示例 1：

		输入：s = "aab"
		输出：1
		解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

	示例 2：

		输入：s = "a"
		输出：0

	示例 3：

		输入：s = "ab"
		输出：1

	提示：

		1 <= s.length <= 2000
		s 仅由小写英文字母组成

	link: https://leetcode.cn/problems/palindrome-partitioning-ii/description/
*/

func MinCut_132(s string) int {
	// 初始化缓存与 dp 数组
	cache := make([][]bool, len(s))
	dp := make([]int, len(s))
	for i := range len(s) {
		cache[i] = make([]bool, len(s))
		// 最大分割次数为字符串长度减一，即与索引相同
		dp[i] = i
		for j := range len(s) {
			// 当 j >= i 时，为合法子串，先全部初始化为 true
			cache[i][j] = (j >= i)
		}
	}

	// 更新 cache 中的值
	for i := len(s) - 1; i >= 0; i-- {
		for j := i + 1; j < len(s); j++ {
			// 计算时依赖 dp[i+1][j-1] 的值
			// 所以 i 倒序遍历，j 正序遍历
			if j-i == 1 {
				cache[i][j] = s[i] == s[j]
			} else {
				cache[i][j] = s[i] == s[j] && cache[i+1][j-1]
			}
		}
	}

	// 计算 dp 数组
	for j := range len(s) {
		for i := range j + 1 {
			// 循环判断以 j 结尾作为最后一个回文串时
			// 所需的最小切割次数
			if !cache[i][j] {
				continue
			}
			if i == 0 {
				dp[j] = 0
			} else {
				dp[j] = min(dp[j], dp[i-1]+1)
			}
		}
	}

	return dp[len(s)-1]
}
