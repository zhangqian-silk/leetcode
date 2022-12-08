'''
    在考场里，一排有 N 个座位，分别编号为 0, 1, 2, ..., N-1 。

    当学生进入考场后，他必须坐在能够使他与离他最近的人之间的距离达到最大化的座位上。
    如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在 0 号座位上。)

    返回 ExamRoom(int N) 类，它有两个公开的函数：其中，函数 ExamRoom.seat() 会返回一个 int （整型数据），
    代表学生坐的位置；函数 ExamRoom.leave(int p) 代表坐在座位 p 上的学生现在离开了考场。
    每次调用 ExamRoom.leave(p) 时都保证有学生坐在座位 p 上。

    示例：

    输入：["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
    输出：[null,0,9,4,2,null,5]
    解释：
    ExamRoom(10) -> null
    seat() -> 0，没有人在考场里，那么学生坐在 0 号座位上。
    seat() -> 9，学生最后坐在 9 号座位上。
    seat() -> 4，学生最后坐在 4 号座位上。
    seat() -> 2，学生最后坐在 2 号座位上。
    leave(4) -> null
    seat() -> 5，学生最后坐在 5 号座位上。

    提示：

    1 <= N <= 10^9
    在所有的测试样例中 ExamRoom.seat() 和 ExamRoom.leave() 最多被调用 10^4 次。
    保证在调用 ExamRoom.leave(p) 时有学生正坐在座位 p 上。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/exam-room
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.seat_num = N
        self.seats = []

    def seat(self):
        """
        :rtype: int
        """
        res = i = 0
        seat_1 = seat_2 = -1
        lenth = len(self.seats)
        # 判断 0 到第一个有人的座位的距离
        if self.seats:
            max_distent = self.seats[0] - 1
            seat_1 = seat_2 = self.seats[0]
            i += 1
        while i < lenth:
            seat_2 = self.seats[i]
            # num = seat_2 - seat_1 - 1 表示两个座位间空座位数量
            # 若空座位数量为奇数，distent = num//2 = (num-1)//2
            # 若空座位数量为偶数，distent = num//2 - 1 = (num-1)//2
            distent = (seat_2 - seat_1 - 1 - 1) // 2
            if distent > max_distent:
                max_distent = distent
                res = seat_1 + max_distent + 1
            seat_1 = seat_2
            i += 1
        # 判断最后一个座位到第 N 个座位的距离
        if self.seats:
            if self.seat_num-1 - seat_2 - 1 > max_distent:
                res = self.seat_num - 1
        self.seats.append(res)
        self.seats.sort()
        return res

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.seats.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)