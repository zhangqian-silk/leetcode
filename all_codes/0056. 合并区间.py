'''
    给出一个区间的集合，请合并所有重叠的区间。

    示例 1:

    输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

    示例 2:

    输入: intervals = [[1,4],[4,5]]
    输出: [[1,5]]
    解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
    
    注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。

    提示：

    intervals[i][0] <= intervals[i][1]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/merge-intervals
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if len(intervals) <= 0:
            return []
        intervals.sort(key=lambda x:(x[0], -x[1]))
        end = intervals[0][1]
        i = 1
        while i < len(intervals):
            # 相离
            if end < intervals[i][0]:
                end = intervals[i][1]
                i += 1
            # 包含
            elif end >= intervals[i][1]:
                del(intervals[i])
            # 相交
            elif end < intervals[i][1]:
                intervals[i-1][1] = intervals[i][1]
                end = intervals[i][1]
                del(intervals[i])
        return intervals
                
