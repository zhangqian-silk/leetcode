// 给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。
//
// 进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？
//
// 示例：
//
// 输入：root = [1,3,null,null,2]
// 输出：[3,1,null,null,2]
// 解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
//
// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/recover-binary-search-tree
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

// 中序遍历
// preroot指向上一个操作的节点
void inorderTravel(struct TreeNode* root, struct TreeNode** preroot, struct TreeNode** first){
    if(root == NULL)
        return; 
    inorderTravel(root->left, preroot, first);
    if((*preroot) != NULL){
        // 错误的第一个节点，该节点大于他后面的数，即preroot错误
        if((*preroot)->val > root->val && (*first) == NULL)
            (*first) = (*preroot);
        // 错误的第二个节点，第一个大于该节点的前一个位置，是第一个错误节点的正确位置
        if((*first) != NULL && root->val > (*first)->val){
            int i = (*first)->val;
            (*first)->val = (*preroot)->val;
            (*preroot)->val = i;
            return;
        } 
    }
    (*preroot) = root;
    inorderTravel(root->right, preroot, first);
}

void recoverTree(struct TreeNode* root){
    if(root == NULL)
        return;
    struct TreeNode* first = NULL;
    struct TreeNode* preroot = NULL;
    inorderTravel(root, &preroot, &first);
    // 如果第二个错误节点在最后，则上述遍历不能完成交换
    // 此时first中val应该为大值，且preroot指向最后一个节点
    if(first->val > preroot->val){
        int i = first->val;
        first->val = preroot->val;
        preroot->val = i;
    }
    return;
}