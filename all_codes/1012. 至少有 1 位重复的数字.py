'''
给定正整数 n，返回在 [1, n] 范围内具有 至少 1 位 重复数字的正整数的个数。

 

示例 1：

输入：n = 20
输出：1
解释：具有至少 1 位重复数字的正数(<= 20)只有 11 。
示例 2：

输入：n = 100
输出：10
解释：具有至少 1 位重复数字的正数(<= 100)有 11，22，33，44，55，66，77，88，99 和 100 。
示例 3：

输入：n = 1000
输出：262
 

提示：

1 <= n <= 10^9

https://leetcode.cn/problems/numbers-with-repeated-digits/
'''

# 计算排列数
def aValue(n: int, m: int) -> int:
    a = 1
    for i in range(m):
        a *= (n - i)
    return a

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        # 计算所有小于 n 的，不重复的数字，然后与 n 取差值
        numSet = set()
        numCount = 0
        arr = list(map(int, str(n)))
        length = len(arr)

        for i in range(length-1):
            # 处理当前及之前位置为 0 且后一位不为 0 的场景
            numCount += 9 * aValue(9, length-(i+1)-1)
            
            if i > len(numSet):
                # 之前位置的最大数字出现重复，不用再继续遍历
                continue
            
            for j in range(arr[i]):
                # 在前面位置的数字取最大值的场景下，
                # 循环判断当前位置的数字，在合法取值时，不重复的数字的数量
                if j == 0 and len(numSet) == 0:
                    # 首位为 0 的场景，在之前已被统计过，直接跳过
                    continue
                if j not in numSet:
                    # 若当前位置未取得最大值，后面数字可任意取值，直接计算排列数即可
                    numCount += aValue(9-len(numSet), length-(i+1))
            # 当前及之前位置均取最大值时，再判读后续数字
            numSet.add(arr[i])
        
        # 在前面位置数字最大值均不一样的场景下，最后一位数字，单独处理
        if length-1 == len(numSet):
            for k in range(arr[length-1]+1):
                if k == 0 and len(numSet) == 0:
                    # 个位数字的异常情况，此时 0 不算正数，不计数
                    continue
                if k not in numSet:
                    numCount += 1
        return n-numCount
    
n = 110
res = Solution().numDupDigitsAtMostN(n)

print(res)
