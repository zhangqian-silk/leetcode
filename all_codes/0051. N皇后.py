'''
    n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

    上图为 8 皇后问题的一种解法。

    给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

    每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

    示例：

    输入：4
    输出：
    [
        [".Q..",  // 解法 1
        "...Q",
        "Q...",
        "..Q."],

        ["..Q.",  // 解法 2
        "Q...",
        "...Q",
        ".Q.."]
    ]
    解释: 4 皇后问题存在两个不同的解法。

    提示：

    皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/n-queens
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 判断放入的棋子在对角线上是否存在其他旗子
        def isvaild(row, col):
            for i in range(1, row+1):
                if col-i >= 0:
                    if res[row-i][col-i] == 'Q':
                        return False
                if col+i <= n:
                    if res[row-i][col+i] == 'Q':
                        return False
            return True 

        def backstrack(row = 0):
            if row == n:
                all_res.append(res[:])
            else:
                for i in range(n):
                    # 判断放入的旗子在列上是否存在其他旗子
                    if i in num:
                        continue
                    num.append(i)
                    
                    # 在坐标(row,i)放入一个旗子，
                    queen = ""
                    for j in range(n):
                        if j == i:
                            queen += "Q"
                        elif j != i:
                            queen += "."
                    res.append(queen)

                    #如果可以放入该旗子，就去放下一行
                    if isvaild(row, i):
                        backstrack(row+1)

                    #撤销这一行的操作
                    del(num[-1])
                    del(res[-1])
                    
        num = []
        res = []
        all_res = []
        backstrack()
        return all_res

        