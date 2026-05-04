class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def find_target(root: TreeNode | None, k: int) -> bool:
    seen = set()
    if not root:
        return 

    def dfs(node: TreeNode | None) -> bool:
        if not node:
            return False

        if k - node.val in seen:
            return True
        
        seen.add(node.val)

        return dfs(node.left) or dfs(node.right)
    
    return dfs(root, k)

