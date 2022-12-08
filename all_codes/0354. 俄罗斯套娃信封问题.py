'''
    给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。
    当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

    请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

    说明:
    不允许旋转信封。

    示例:

    输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
    输出: 3 
    解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/russian-doll-envelopes
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        lenth = len(envelopes)
        if lenth <= 1:
            return lenth
        envelopes.sort(key= lambda x:(x[0], -x[1]))
        res = 1
        max_nums = [1 for _ in range(lenth)]
        for i in range(lenth):
            max_num = 1
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    max_num = max(max_num, max_nums[j]+1)
            max_nums[i] = max_num
            res = max(res, max_num)
        return res