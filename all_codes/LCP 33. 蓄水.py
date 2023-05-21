'''
给定 N 个无限容量且初始均空的水缸，每个水缸配有一个水桶用来打水，第 i 个水缸配备的水桶容量记作 bucket[i]。小扣有以下两种操作：

升级水桶：选择任意一个水桶，使其容量增加为 bucket[i]+1
蓄水：将全部水桶接满水，倒入各自对应的水缸
每个水缸对应最低蓄水量记作 vat[i]，返回小扣至少需要多少次操作可以完成所有水缸蓄水要求。

注意：实际蓄水量 达到或超过 最低蓄水量，即完成蓄水要求。

示例 1：

输入：bucket = [1,3], vat = [6,8]

输出：4

解释： 第 1 次操作升级 bucket[0]； 第 2 ~ 4 次操作均选择蓄水，即可完成蓄水要求。vat1.gif

示例 2：

输入：bucket = [9,0,1], vat = [0,2,2]

输出：3

解释： 第 1 次操作均选择升级 bucket[1] 第 2~3 次操作选择蓄水，即可完成蓄水要求。

提示：

1 <= bucket.length == vat.length <= 100
0 <= bucket[i], vat[i] <= 10^4
'''

from math import ceil
from typing import List

class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        res = 0
        upTime = 0
        maxAddTime = 0
        # 第一次遍历，计算出全部选择蓄水时，需要的次数
        for i in range(len(bucket)):
            # bucket[i] == 0 时，如果 vat[i] > 0，一定需要升级、
            # 如果 vat[i] == 0，则不需要升级，此时 bucket[i] 自增方便除法运算，不会影响最终结果
            if bucket[i] == 0:
                bucket[i] += 1
                if vat[i] > 0:
                    upTime += 1
            
            maxAddTime = max(ceil(vat[i] / bucket[i]), maxAddTime)
        res = upTime + maxAddTime

        print("up time = " + str(upTime))
        print("add time = " + str(maxAddTime))
        print("----------")

        for addTime in range(maxAddTime, 0, -1):
            # 计算每次减少蓄水次数时，需要升级的次数，并更新最终的操作次数
            for j in range(len(bucket)):
                while bucket[j] * addTime < vat[j]:
                    bucket[j] += 1
                    upTime += 1
            print("up time = " + str(upTime))
            print("add time = " + str(addTime))
            print("----------")
            res = min(res, addTime + upTime)

        return res

bucket = [1,3]
vat = [6,8]
res = Solution().storeWater(bucket, vat)
print(res)