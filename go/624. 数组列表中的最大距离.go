package main

/*
	给定 m 个数组，每个数组都已经按照升序排好序了。

	现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。两个整数 a 和 b 之间的距离定义为它们差的绝对值 |a-b| 。

	返回最大距离。

	示例 1：

		输入：[[1,2,3],[4,5],[1,2,3]]
		输出：4
		解释：
		一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。

	示例 2：

		输入：arrays = [[1],[1]]
		输出：0

	提示：

		m == arrays.length
		2 <= m <= 105
		1 <= arrays[i].length <= 500
		-104 <= arrays[i][j] <= 104
		arrays[i] 以 升序 排序。
		所有数组中最多有 105 个整数。

	link: https://leetcode.cn/problems/maximum-distance-in-arrays/description/
*/

func MaxDistance624(arrays [][]int) int {
	var minValue, minIndex, maxValue, maxIndex, lastMinValue, lastMaxValue int
	for i, arr := range arrays {
		curMin := arr[0]
		curMax := arr[len(arr)-1]
		if i == 0 {
			minValue = curMin
			maxValue = curMax
			continue
		}

		if curMin < minValue {
			// 更新最小值和次小值
			lastMinValue = minValue
			minValue = curMin
			minIndex = i
		} else if i == 1 || curMin < lastMinValue {
			// 单独更新次小值
			// 次小值和最小值的初始值均为索引 0 对应元素
			// 针对 i 为 1 且未触发更新的场景，强制更新次小值
			lastMinValue = curMin
		}

		if curMax > maxValue {
			lastMaxValue = maxValue
			maxValue = curMax
			maxIndex = i
		} else if i == 1 || curMax > lastMaxValue {
			lastMaxValue = curMax
		}
	}

	var res int
	if maxIndex != minIndex {
		res = maxValue - minValue
	} else {
		res = max(maxValue-lastMinValue, lastMaxValue-minValue)
	}
	return res
}
