// 给定一个二叉树，检查它是否是镜像对称的。
//
// 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
//
//     1
//    / \
//   2   2
//  / \ / \
// 3  4 4  3
//  
//
// 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
//
//     1
//    / \
//   2   2
//    \   \
//    3    3
//
// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/symmetric-tree
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* new_root;

bool isSymmetric(struct TreeNode* root){
    if(root == NULL)
        return true;
    else if(root->left == NULL && root->right == NULL)
        return true;
    else if(root->left == NULL || root->right == NULL)
        return false;
    else if((root->left)->val != (root->right)->val)
        return false;
    else{
        new_root = root->left->right;
        root->left->right = root->right->right;
        root->right->right = new_root;
        return isSymmetric(root->left) && isSymmetric(root->right);
    }
}