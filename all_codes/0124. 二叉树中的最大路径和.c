// 给定一个非空二叉树，返回其最大路径和。
//
// 本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
//
// 示例 1：
//
// 输入：[1,2,3]
//
//        1
//       / \
//      2   3
//
// 输出：6
//
// 示例 2：
//
// 输入：[-10,9,20,null,null,15,7]
//
//    -10
//    / \
//   9  20
//     /  \
//    15   7
//
// 输出：42
//
// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

// 后序遍历，比较左右子树的值和0的大小，父节点的值加上三者的最大值
// 同时，比较当前的路径最大值和走当前遍历节点和其两个子节点中任意节点的值，取较大值来更新路径最大值
int max_cmp(int a, int b){
    return a>b ? a : b;
}

int postorderTraversal(struct TreeNode* root, int* max_num){
    if(root == NULL)
        return 0;
    int left_num = max_cmp(0, postorderTraversal(root->left, max_num));
    int right_num = max_cmp(0, postorderTraversal(root->right, max_num));
    (*max_num) = max_cmp((*max_num), root->val + left_num + right_num);
    return root->val + max_cmp(left_num, right_num);
}

int maxPathSum(struct TreeNode* root){
    if(root == NULL)
        return -1;
    int max_num = root->val;
    postorderTraversal(root, &max_num);
    return max_num;
}