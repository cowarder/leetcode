"""
问题描述：

98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""

"""
解题思路：
问题考察的是判断是否是一个合理的二叉查找树
给定当前根结点的上下范围
访问左子树的时候更新上界，当前节点值为左子树上界
访问右子树的时候更新下界，当前节点值为右子树下界
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root, floor=float("inf"), ceil=float("inf")):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True
        if root.val <= floor or root.val >= ceil:
            return False
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceil)