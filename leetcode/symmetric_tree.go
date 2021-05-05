// Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

// Example 1:
//     Input: root = [1,2,2,3,4,4,3]
//     Output: true

// Example 2:
//     Input: root = [1,2,2,null,3,null,3]
//     Output: false

// Constraints:
//     The number of nodes in the tree is in the range [1, 1000].
//     -100 <= Node.val <= 100

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isSymmetric(root *TreeNode) bool {
	return sym(root.Left, root.Right)
}

func sym(t1 *TreeNode, t2 *TreeNode) bool {
	if t1 == nil {
		return t2 == nil
	}
	if t2 == nil {
		return t1 == nil
	}
	return t1.Val == t2.Val &&
		sym(t1.Left, t2.Right) &&
		sym(t1.Right, t2.Left)
}
