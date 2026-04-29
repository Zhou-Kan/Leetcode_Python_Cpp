import java.util.*;
public class Solution {
    class TreeNode{
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
        TreeNode(int val) {
            this(val, null, null);
        }
    }

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null) return ans;
        Deque<TreeNode> dq = new ArrayDeque<>();
        dq.addLast(root);
        while (!dq.isEmpty()) {
            List<Integer> curLevel = new ArrayList<>();
            int size = dq.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = dq.removeFirst();
                curLevel.add(node.val);
                if(node.left != null) dq.addLast(node.left);
                if(node.right != null) dq.addLast(node.right);
            }
            ans.add(curLevel);
        }
        return ans;
    }
    
}
