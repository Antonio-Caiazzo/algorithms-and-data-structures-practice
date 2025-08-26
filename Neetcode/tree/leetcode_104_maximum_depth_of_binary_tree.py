# LeetCode 104 - Maximum Depth of Binary Tree (Easy)
#
# Given the root of a binary tree, return its maximum depth.
# The maximum depth is the number of nodes along the longest path
# from the root down to the farthest leaf node.
#
# Examples:
# Input:  root = [3,9,20,null,null,15,7]  -> Output: 3
# Input:  root = [1,null,2]               -> Output: 2
#
# Time complexity: O(n), where n is the number of nodes
# Space complexity: O(h) for recursion stack, where h is tree height (O(n) worst-case)

from typing import Optional, List
from collections import deque

# Definition for a binary tree node (LeetCode style).
class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))

        return dfs(root)


# -----------------------------
# Helpers per i test
# -----------------------------
def build_tree_level_order(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Costruisce un albero binario da una lista level-order con `None` per assenze."""
    if not values:
        return None
    it = iter(values)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q = deque([root])
    for v_left, v_right in zip(it, it):
        node = q.popleft()
        if v_left is not None:
            node.left = TreeNode(v_left)
            q.append(node.left)
        if v_right is not None:
            node.right = TreeNode(v_right)
            q.append(node.right)
    return root


# -----------------------------
# Test cases for Maximum Depth of Binary Tree
# -----------------------------
def test_max_depth():
    print("Running test cases for Maximum Depth of Binary Tree...")
    sol = Solution()

    # Example 1
    root = build_tree_level_order([3,9,20,None, None, 15, 7])
    assert sol.maxDepth(root) == 3, "Test 1 failed"

    # Example 2
    root = build_tree_level_order([1, None, 2])
    assert sol.maxDepth(root) == 2, "Test 2 failed"

    # Edge cases
    assert sol.maxDepth(None) == 0, "Test 3 failed"                     # empty tree
    root = build_tree_level_order([1])                                   # single node
    assert sol.maxDepth(root) == 1, "Test 4 failed"

    # Skewed left
    root = build_tree_level_order([1,2,None,3,None,4,None])
    assert sol.maxDepth(root) == 4, "Test 5 failed"

    # Full balanced tree depth 3
    root = build_tree_level_order([1,2,3,4,5,6,7])
    assert sol.maxDepth(root) == 3, "Test 6 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_max_depth()
