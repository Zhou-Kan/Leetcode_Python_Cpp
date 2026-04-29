#include<iostream>
//#include<deque>
class TreeNode{
    public:
        int val;
        TreeNode* left;
        TreeNode* right;
        TreeNode(): val(val), left(left), right(right) {}
};

std::vector<std::vector<int>> levelOrder(TreeNode* root) {
    std::deque<TreeNode*> dq;
    std::vector<std::vector<int>> ans;
    if (!root) return ans;
    dq.push_back(root);
    while (!dq.empty()) {
        int size = dq.size();
        std::vector<int> curLevel;
        for(int i = 0; i < size; i++) {
            TreeNode* node = dq.front();
            curLevel.push_back(node->val);
            dq.pop_front();
            if(node->left) dq.push_back(node->left);
            if(node->right) dq.push_back(node->right);
        }
        ans.push_back(curLevel);
    }
    return ans;
}