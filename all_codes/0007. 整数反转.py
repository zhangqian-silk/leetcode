'''
    给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

    示例 1:

    输入: 123
    输出: 321
     示例 2:

    输入: -123
    输出: -321
    示例 3:

    输入: 120
    输出: 21
    注意:

    假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/reverse-integer
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        list_num = list(str(x))
        right = len(list_num) - 1
        left = 0
        
        # 判断符号
        if list_num[0] == '-':
            left += 1
        
        # 反转列表
        while left < right:
            num = list_num[left]
            list_num[left] = list_num[right]
            list_num[right] = num
            left += 1
            right -= 1
        
        res = int(''.join(list_num))

        if res > 2**31-1 or res < -(2**31):
            return 0
        else:
            return res
