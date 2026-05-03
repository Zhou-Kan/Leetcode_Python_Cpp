#include <unordered_set>
class TreeNode {
    public: 
        int val;
        TreeNode* left;
        TreeNode* right;
        TreeNode(int val) : val(val), left(nullptr), right(nullptr) {}
        TreeNode(int val, TreeNode* left, TreeNode* right) : val(val), left(left), right(right) {}
};

class Solution {
    public:
        bool dfs(TreeNode* root, int k, std::unordered_set<int>& s) {
            if(!root) return false;
            if (s.count(k - root->val)) return true;
            s.insert(root->val);
            return dfs(root->left, k, s) || dfs(root->right, k, s);
        }

        bool findTarget(TreeNode* root, int k) {
            std::unordered_set<int> s;
            return dfs(root, k, s);
        }
};

int main() {
    TreeNode* node1 = new TreeNode(0);
    return 0;
}