/* Invert a binary tree.
 *
 * Example:
 *
 *  Input:
 *
 *       4
 *     /   \
 *    2     7
 *   / \   / \
 *  1   3 6   9
 *
 *  Output:
 *
 *       4
 *     /   \
 *    7     2
 *   / \   / \
 *  9   6 3   1
 *
 *  Trivia:
 *  This problem was inspired by this original tweet by Max Howell:
 *
 *      Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
 */

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	tmp := root.Left
	root.Left = root.Right
	root.Right = tmp
	if root.Left != nil {
		invertTree(root.Left)
	}
	if root.Right != nil {
		invertTree(root.Right)
	}
	return root
}
