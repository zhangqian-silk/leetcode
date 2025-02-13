package main

import "slices"

/*
	给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

	字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

	示例 1:

		输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
		输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

	示例 2:

		输入: strs = [""]
		输出: [[""]]

	示例 3:

		输入: strs = ["a"]
		输出: [["a"]]

	提示：

		1 <= strs.length <= 10^4
		0 <= strs[i].length <= 100
		strs[i] 仅包含小写字母

	link: https://leetcode.cn/problems/group-anagrams/description/
*/

func GroupAnagrams(strs []string) [][]string {
	if len(strs) <= 1 {
		return [][]string{strs}
	}

	// 将字符串排序后，用 map 做聚合
	resMap := make(map[string][]string)
	for _, str := range strs {
		strList := []byte(str)
		slices.Sort(strList)
		finalStr := string(strList)
		resMap[finalStr] = append(resMap[finalStr], str)
	}

	res := make([][]string, 0, len(resMap))
	for _, v := range resMap {
		res = append(res, v)
	}
	return res
}
