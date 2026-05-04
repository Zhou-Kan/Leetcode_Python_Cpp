class TreeNode{
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

function levelOrder(root: TreeNode | null): number[][] {
    if (!root) return []
    const dq: TreeNode[] = []
    const ans: number[][] = []
    dq.push(root)
    let head = 0;
    while (head < dq.length) {
        const curLevel: number[] = []
        const size = dq.length - head
        for(let j = 0; j < size; j++) {
            const node = dq[head++]
            curLevel.push(node.val)
            if (node.left) dq.push(node.left)
            if (node.right) dq.push(node.right)
        }
        ans.push(curLevel)
    }
    return ans
}