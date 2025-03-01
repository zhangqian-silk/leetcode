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

	var dfs func(idx int, curString string, curRes []string)
	dfs = func(idx int, curString string, curRes []string) {
		if idx == len(s) {
			// 遍历结束，最后一次判断
			if check_131(curString) {
				// 深拷贝，避免 res 被修改
				newRes := make([]string, len(curRes))
				copy(newRes, curRes)
				res = append(res, append(newRes, curString))
			}
			return
		}

		// 选择当前字符继续拼接子串，则加上当前字符继续递归
		newString := curString + string(s[idx])
		// 记录当前切片长度，后续从该长度进行剪切
		curLength := len(curRes)
		dfs(idx+1, newString, curRes)
		// 不选择当前字符拼接子串，则判断之前的子串是否为回文串
		if check_131(curString) {
			// 如果之前的子串构成回文串，则添加至 res 中
			dfs(idx+1, string(s[idx]), append(curRes[:curLength], curString))
		}
	}
	dfs(0, "", nil)
	return res
}
