# LeetCode 226 - Invert Binary Tree (Easy)
#
# Given the root of a binary tree, invert the tree, and return its root.
#
# Examples:
# Input:  root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
# Input:  root = [2,1,3]
# Output: [2,3,1]
#
# Input:  root = []
# Output: []
#
# Constraints:
# - Number of nodes in the tree is in the range [0, 100]
# - -100 <= Node.val <= 100
#
# Time complexity: O(n), where n = number of nodes
# Space complexity: O(h), recursion stack (h = height of the tree, O(n) worst-case)

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# -----------------------------
# Helpers per i test
# -----------------------------
def build_tree_level_order(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Costruisce un albero binario da lista level-order con `None` per nodi mancanti.
    Gestisce correttamente anche liste di lunghezza dispari (nodi spaiati all'ultimo livello).
    """
    if not values:
        return None
    it = iter(values)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q = deque([root])

    while q:
        node = q.popleft()

        # Left child
        try:
            v_left = next(it)
        except StopIteration:
            break
        if v_left is not None:
            node.left = TreeNode(v_left)
            q.append(node.left)

        # Right child
        try:
            v_right = next(it)
        except StopIteration:
            break
        if v_right is not None:
            node.right = TreeNode(v_right)
            q.append(node.right)

    return root


def tree_to_list_level_order(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Converte un albero in lista level-order (come su LeetCode), rimuovendo i None finali superflui."""
    if not root:
        return []
    res: List[Optional[int]] = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            res.append(None)
            continue
        res.append(node.val)
        q.append(node.left)
        q.append(node.right)

    # Rimuovi None finali
    while res and res[-1] is None:
        res.pop()
    return res


# -----------------------------
# Test cases for Invert Binary Tree
# -----------------------------
def test_invert_binary_tree():
    print("Running test cases for Invert Binary Tree...")
    sol = Solution()

    # Example 1
    root = build_tree_level_order([4,2,7,1,3,6,9])
    inverted = sol.invertTree(root)
    assert tree_to_list_level_order(inverted) == [4,7,2,9,6,3,1], "Test 1 failed"

    # Example 2
    root = build_tree_level_order([2,1,3])
    inverted = sol.invertTree(root)
    assert tree_to_list_level_order(inverted) == [2,3,1], "Test 2 failed"

    # Example 3: empty
    root = build_tree_level_order([])
    inverted = sol.invertTree(root)
    assert tree_to_list_level_order(inverted) == [], "Test 3 failed"

    # Extra: skewed tree (sinistro) -> diventa skewed destro
    root = build_tree_level_order([1,2,None,3,None,4])
    inverted = sol.invertTree(root)
    assert tree_to_list_level_order(inverted) == [1, None, 2, None, 3, None, 4], "Test 4 failed"

    # Extra: skewed tree (destro) -> diventa skewed sinistro
    root = build_tree_level_order([1, None, 2, None, 3, None, 4])
    inverted = sol.invertTree(root)
    # Atteso: catena a sinistra: [1,2,None,3,None,4]
    assert tree_to_list_level_order(inverted) == [1, 2, None, 3, None, 4], "Test 5 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_invert_binary_tree()
