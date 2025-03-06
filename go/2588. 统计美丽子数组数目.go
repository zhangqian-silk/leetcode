package main

func beautifulSubarrays(nums []int) int64 {
	var res int64
	preMap := make(map[int]int64)
	preMap[0] = 1
	mask := 0
	for _, num := range nums {
		mask ^= num
		// 如果 i...j 满足异或结果为 0
		// 则 0...i-1 的异或结果一定与 0...j 的异或结果相同
		res += preMap[mask]
		preMap[mask]++
	}
	return res
}
