'''
    实现一个基本的计算器来计算一个简单的字符串表达式的值。

    字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

    示例 1:

    输入: "1 + 1"
    输出: 2

    示例 2:

    输入: " 2-1 + 2 "
    输出: 3

    示例 3:

    输入: "(1+(4+5+2)-3)+(6+8)"
    输出: 23

    说明：

    你可以假设所给定的表达式都是有效的。
    请不要使用内置的库函数 eval。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/basic-calculator
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def func(s, i = 0):
            stack = []
            lenth = len(s)
            flag = '+'
            while i < lenth:
                if s[i].isdigit():
                    num = 0
                    while(i < lenth and s[i].isdigit()):
                        num = num*10 + int(s[i])
                        i += 1
                    if flag == '-':
                        num *= (-1)
                    elif flag == '*':
                        num = stack.pop(-1) * num
                    elif flag == '/':
                        num = stack.pop(-1) // num
                    stack.append(num)
                    flag = '+'
                elif s[i] == '(':
                    num, i = func(s, i+1)
                    if flag == '-':
                        num *= (-1)
                    elif flag == '*':
                        num = stack.pop(-1) * num
                    elif flag == '/':
                        num = stack.pop(-1) // num
                    stack.append(num)
                    flag = '+'
                elif s[i] == ')':
                    res = 0
                    for val in stack:
                        res += val
                    return res, i+1
                elif s[i] == ' ':
                    i += 1
                else:
                    flag = s[i]
                    i += 1
            res = 0
            for val in stack:
                res += val
            return res,i

        res,_ = func(s)
        return res