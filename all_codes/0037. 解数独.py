'''
    编写一个程序，通过填充空格来解决数独问题。

    一个数独的解法需遵循如下规则：

        数字 1-9 在每一行只能出现一次。
        数字 1-9 在每一列只能出现一次。
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

    空白格用 '.' 表示。

    示例:

    输入:
    [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    输出:
    [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/sudoku-solver
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # col，row，block分别表示行，列，和3x3的方格
        col_num = []
        row_num = []
        block_num = []
        index = 1
        while index <= 9:
            col_num.append(set())
            row_num.append(set())
            block_num.append(set())
            index += 1

        # 填入初始数字
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != "." :
                    block = (i//3)*3 + j//3
                    row_num[i].add(c)
                    col_num[j].add(c)
                    block_num[block].add(c)


        # 开始填数字
        global res
        res = False
        def func(i = 0, j = 0):     
            global res       
            if res == True:
                return
            if j == 9:
                if i == 8 :
                    res = True
                    return
                else:
                    j = 0
                    i += 1
            
            block = (i//3)*3 + j//3
            c = board[i][j]
            if c == "." :
                for k in range(1,10):
                    k = str(k)
                    if (k not in row_num[i]) and (k not in col_num[j]) and (k not in block_num[block]):
                        row_num[i].add(k)
                        col_num[j].add(k)
                        block_num[block].add(k)
                        board[i][j] = k
                        func(i, j+1)
                        if res == True:
                            return
                        row_num[i].remove(k)
                        col_num[j].remove(k)
                        block_num[block].remove(k)
                        board[i][j] = "."
            else:
                func(i, j+1)

        func()
