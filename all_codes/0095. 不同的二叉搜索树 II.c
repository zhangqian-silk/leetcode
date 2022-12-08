// 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
//
// 示例：
//
// 输入：3
// 输出：
// [
//   [1,null,3,2],
//   [3,2,null,1],
//   [3,1,null,null,2],
//   [2,1,3],
//   [1,null,2,null,3]
// ]
// 解释：
// 以上的输出对应以下 5 种不同结构的二叉搜索树：
//
//    1         3     3      2      1
//     \       /     /      / \      \
//      3     2     1      1   3      2
//     /     /       \                 \
//    2     1         2                 3
//
// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode** buildTree(int begin, int end, int* returnSize){  
    if(end < begin){
        struct TreeNode** array_tree = (struct TreeNode**)malloc(sizeof(struct TreeNode*));
        array_tree[(*returnSize)++] = NULL;
        return array_tree;
    }

    int i = begin;
    struct TreeNode** array_tree = (struct TreeNode**)malloc(0);
    for(; i <= end; i++){
        // 构造左右子树
        int left_size = 0;
        struct TreeNode** left_tree = buildTree(begin, i-1, &left_size);
        
        int right_size = 0;
        struct TreeNode** right_tree = buildTree(i+1, end, &right_size);
        
        int m, n;
        for(m = 0; m < left_size; m++){
            for(n = 0; n < right_size; n++){
                struct TreeNode* tree = (struct TreeNode*)malloc(sizeof(struct TreeNode));
                tree->val = i;
                tree->left = left_tree[m];
                tree->right = right_tree[n];
                (*returnSize)++;
                array_tree = (struct TreeNode**)realloc(array_tree,sizeof(struct TreeNode*)*(*returnSize));
                array_tree[(*returnSize)-1] = tree;
            }
        }    

        free(left_tree);
        free(right_tree);
    }
    
    return array_tree;
}

struct TreeNode** generateTrees(int n, int* returnSize){
    *returnSize = 0;
    if(n == 0)
        return NULL;
    return buildTree(1, n, returnSize);
}