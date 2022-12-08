'''
    判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

        数字 1-9 在每一行只能出现一次。
        数字 1-9 在每一列只能出现一次。
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

    数独部分空格内已填入了数字，空白格用 '.' 表示。

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
    输出: true

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/valid-sudoku
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # col，row，block分别表示行，列，和3x3的方格
        col_num = []
        row_num = []
        block_num = []
        for i in range(9):
            col_num.append([])
            row_num.append([])
            block_num.append([])
        
        # 把每一个数字放入对应的行列表，列列表，3x3方格列表
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != "." :
                    block = (i//3)*3 + j//3
                    # 判断是否有效
                    if (c in row_num[i]) or (c in col_num[j]) or (c in block_num[block]):
                        return False
                    else:
                        row_num[i].append(c)
                        col_num[j].append(c)
                        block_num[block].append(c)
        return True
