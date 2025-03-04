package main

/*
	给你一个字符串 s ，如果可以将它分割成三个 非空 回文子字符串，那么返回 true ，否则返回 false 。

	当一个字符串正着读和反着读是一模一样的，就称其为 回文字符串 。

	示例 1：

		输入：s = "abcbdd"
		输出：true
		解释："abcbdd" = "a" + "bcb" + "dd"，三个子字符串都是回文的。

	示例 2：

		输入：s = "bcbddxy"
		输出：false
		解释：s 没办法被分割成 3 个回文子字符串。

	提示：

		3 <= s.length <= 2000
		s​​​​​​ 只包含小写英文字母。

	link: https://leetcode.cn/problems/palindrome-partitioning-iv/description/
*/
func CheckPartitioning_1745(s string) bool {
	// dp[i][j] 表示前 j 个字符，能否分割成 i 个回文串
	// 如果当前字符需要新进行分割，dp[i][j] = dp[i-1][j-1]
	//
	// 如果当前字符不重新进行分割，则需要与其他字符进行合并
	// 并判断合并以外的部分，能否分为成 i-1 个字符串，即：
	// 当 n~j 为回文串，且 dp[i-1][n-1] (i-1 <= n < j) 为 true 时，dp[i][j] = true
	//
	// i 只与 i-1 相关，所以只用两个数组即可
	dp := make([]bool, len(s))
	lastDp := make([]bool, len(s))

	// 初始化缓存与 dp 数组
	cache := make([][]bool, len(s))
	for i := range len(s) {
		cache[i] = make([]bool, len(s))
		for j := range len(s) {
			// 当 j >= i 时，为合法子串，先全部初始化为 true
			cache[i][j] = (j >= i)
		}
	}

	// 更新 cache 中的值
	for i := len(s) - 1; i >= 0; i-- {
		for j := i; j < len(s); j++ {
			// 计算时依赖 dp[i+1][j-1] 的值
			// 所以 i 倒序遍历，j 正序遍历
			if j-i <= 1 {
				cache[i][j] = s[i] == s[j]
			} else {
				cache[i][j] = s[i] == s[j] && cache[i+1][j-1]
			}

			// 切割后数量为 1 时，直接判断该子串是否为回文串即可
			if i == 0 {
				lastDp[j] = cache[i][j]
			}
		}
	}

	// 从 i = 2，即能否切割为 2 个子串开始判断
	for i := 2; i <= 3; i++ {
		// 索引为 i-1 时，子串长度等于 i，一定满足条件
		dp[i-1] = true
		for j := i; j < len(s); j++ {
			flag := false
			for n := i - 1; n <= j; n++ {
				if !cache[n][j] {
					continue
				}
				if lastDp[n-1] {
					flag = true
					break
				}
			}
			dp[j] = flag
		}
		// 更新 lastDP 为当前切片，旧有数据可以丢弃
		lastDp, dp = dp, lastDp
	}

	return lastDp[len(s)-1]
}
