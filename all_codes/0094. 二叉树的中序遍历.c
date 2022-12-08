// 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
//  
// 示例：
// 输入：root = [1,null,2,3]
// 输出：[1,3,2]
//
// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//给定一个二叉树的根节点 root ，返回它的 中序 遍历。

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

//递归
void inorder(struct TreeNode* root, int* res, int* returnSize){
    if(root == NULL)
        return;
    inorder(root->left, res, returnSize);
    res[(*returnSize)++] = root->val;
    inorder(root->right, res, returnSize);
}

int* inorderTraversal1(struct TreeNode* root, int* returnSize){
    int* res = (int*)malloc(sizeof(int)*100);
    *returnSize = 0;
    inorder(root, res, returnSize);
    return res;
}

//栈实现迭代
int* inorderTraversal2(struct TreeNode* root, int* returnSize){
    int* res = (int*)malloc(sizeof(int)*100);
    *returnSize = 0;
    struct TreeNode** stack_tree = (struct TreeNode**)malloc(sizeof(struct TreeNode*)*100);
    int top = 0;
    while(root != NULL || top > 0){
        while(root != NULL){
            stack_tree[top++] = root;
            root = root->left;
        }
        root = stack_tree[--top];
        res[(*returnSize)++] = root->val;
        root = root->right;
    }
    free(stack_tree);
    return res;
}