// 斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
//
// F(0) = 0,   F(1) = 1
// F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
// 给定 N，计算 F(N)。
//
// 示例 1：
//
// 输入：2
// 输出：1
// 解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
//
// 示例 2：
//
// 输入：3
// 输出：2
// 解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
//
// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/fibonacci-number
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int fib(int N){
    if(N == 0)
        return 0;
    if(N ==1 )
        return 1;
    int num_1 = 0, num_2 = 1, i = 3, num_3 = 0;
    for(; i <= N; i++){
        num_3 = num_1 + num_2;
        num_1 = num_2;
        num_2 = num_3;
    }
    return num_3;
}