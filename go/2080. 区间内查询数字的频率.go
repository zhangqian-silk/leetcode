package main

/*
	请你设计一个数据结构，它能求出给定子数组内一个给定值的 频率 。

	子数组中一个值的 频率 指的是这个子数组中这个值的出现次数。

	请你实现 RangeFreqQuery 类：

	RangeFreqQuery(int[] arr) 用下标从 0 开始的整数数组 arr 构造一个类的实例。
	int query(int left, int right, int value) 返回子数组 arr[left...right] 中 value 的 频率 。
	一个 子数组 指的是数组中一段连续的元素。arr[left...right] 指的是 nums 中包含下标 left 和 right 在内 的中间一段连续元素。

	示例 1：

		输入：
		["RangeFreqQuery", "query", "query"]
		[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
		输出：
		[null, 1, 2]

		解释：
		RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
		rangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
		rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。

	提示：

		1 <= arr.length <= 10^5
		1 <= arr[i], value <= 10^4
		0 <= left <= right < arr.length
		调用 query 不超过 10^5 次。

	link: https://leetcode.cn/problems/range-frequency-queries/description/
*/

type RangeFreqQuery struct {
	indexMap map[int][]int
}

func Constructor(arr []int) RangeFreqQuery {
	indexMap := make(map[int][]int)
	for i, value := range arr {
		indexMap[value] = append(indexMap[value], i)
	}

	return RangeFreqQuery{
		indexMap: indexMap,
	}
}

func (this *RangeFreqQuery) Query(left int, right int, value int) int {
	indexArr := this.indexMap[value]
	// 一定不满足的情况
	if len(indexArr) == 0 ||
		indexArr[0] > right ||
		indexArr[len(indexArr)-1] < left {
		return 0
	}

	// 求大于等于 left 的最小索引
	indexLeft := 0
	indexRight := len(indexArr) - 1
	index1 := 0
	for indexLeft <= indexRight {
		index1 = indexLeft + (indexRight-indexLeft)/2
		if indexArr[index1] < left {
			indexLeft = index1 + 1
		} else if indexArr[index1] > left {
			indexRight = index1 - 1
		} else if indexArr[index1] == left {
			break
		}
	}
	if indexArr[index1] != left {
		index1 = indexLeft
	}

	// 求小于等于 right 的最大索引
	indexLeft = index1
	indexRight = len(indexArr) - 1
	index2 := 0
	for indexLeft <= indexRight {
		index2 = indexLeft + (indexRight-indexLeft)/2
		if indexArr[index2] > right {
			indexRight = index2 - 1
		} else if indexArr[index2] < right {
			indexLeft = index2 + 1
		} else if indexArr[index2] == right {
			break
		}
	}
	if indexArr[index2] != right {
		index2 = indexRight
	}

	if index1 > index2 {
		return 0
	}
	return index2 - index1 + 1
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * obj := Constructor(arr);
 * param_1 := obj.Query(left,right,value);
 */
