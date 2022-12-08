'''
     f(x) 是 x! 末尾是0的数量。（回想一下 x! = 1 * 2 * 3 * ... * x，且0! = 1）

    例如， f(3) = 0 ，因为3! = 6的末尾没有0；而 f(11) = 2 ，因为11!= 39916800末端有2个0。
    给定 K，找出多少个非负整数x ，有 f(x) = K 的性质。

    示例 1:
    输入:K = 0
    输出:5
    解释: 0!, 1!, 2!, 3!, and 4! 均符合 K = 0 的条件。

    示例 2:
    输入:K = 5
    输出:0
    解释:没有匹配到这样的 x!，符合K = 5 的条件。
    注意：

    K是范围在 [0, 10^9] 的整数。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        def func(n):
            res = 0
            val = 5
            while n >= val:
                res += n // val
                val *= 5
            return res
        
        right_num = (10**9)*5
        left_num = 0
        
        # 先找到一个目标值
        while left_num <= right_num:
            mid_num = (left_num + right_num) // 2
            if func(mid_num) == K:
                break
            elif func(mid_num) < K:
                left_num = mid_num+1
            elif func(mid_num) > K:
                right_num = mid_num-1
        # 没有找到
        if left_num > right_num:
            return 0
        leftPart_right = rightPart_left = mid_num
        
        # 找左侧边界，在 left_num 和 leftPart_right 中间
        # 结束时，left_num 为左边界
        while func(left_num) != K:
            leftPart_mid = (left_num + leftPart_right) // 2
            if func(leftPart_mid) == K:
                leftPart_right = leftPart_mid
            elif func(leftPart_mid) < K:
                left_num = leftPart_mid + 1
        
        # 找右侧边界，在 rightPart_left 和 right_num 中间
        # 结束时，rightPart_left-1 为右边界
        while func(rightPart_left) == K:
            rightPart_mid = (rightPart_left + right_num) // 2
            if func(rightPart_mid) == K:
                rightPart_left = rightPart_mid + 1
            elif func(rightPart_mid) > K:
                right_num = rightPart_mid
        
        return rightPart_left - left_num