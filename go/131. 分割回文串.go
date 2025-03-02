package main

/*
	给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

	示例 1：

		输入：s = "aab"
		输出：[["a","a","b"],["aa","b"]]

	示例 2：

		输入：s = "a"
		输出：[["a"]]

	提示：

		1 <= s.length <= 16
		s 仅由小写英文字母组成

	link: https://leetcode.cn/problems/palindrome-partitioning/description/
*/

func check_131(s string) bool {
	if s == "" {
		return false
	}
	left := 0
	right := len(s) - 1
	for left <= right {
		if s[left] != s[right] {
			return false
		}
		left++
		right--
	}
	return true
}

func Partition_131(s string) [][]string {
	var res [][]string
	var curRes []string
	var dfs func(int)
	dfs = func(idx int) {
		if idx == len(s) {
			// 深拷贝，避免 res 被修改
			newRes := make([]string, len(curRes))
			copy(newRes, curRes)
			res = append(res, newRes)
			return
		}

		// 从当前位置开始循环判断，当满足回文串时，
		// 从下一个位置继续递归
		var curStr string
		curLength := len(curRes)
		for i := idx; i < len(s); i++ {
			curStr += string(s[i])
			if !check_131(curStr) {
				continue
			}

			// 将当前字符添加至拆分的结果中，并递归判断剩余字符
			curRes = append(curRes, curStr)
			dfs(i + 1)
			curRes = curRes[:curLength]
		}
	}
	dfs(0)
	return res
}
