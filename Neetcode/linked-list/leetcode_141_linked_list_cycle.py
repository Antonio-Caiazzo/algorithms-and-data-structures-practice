# LeetCode 141 - Linked List Cycle (Easy)
#
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle if some node can be reached again by continuously following next.
# Internally LeetCode uses `pos` to denote the index where tail connects (not passed to the function).
# Return True if there is a cycle, otherwise False.
#
# Examples:
# Input:  head = [3,2,0,-4], pos = 1  -> Output: True
# Input:  head = [1,2],        pos = 0  -> Output: True
# Input:  head = [1],          pos = -1 -> Output: False
#
# Constraints:
# - number of nodes in [0, 10^4]
# - -10^5 <= Node.val <= 10^5
# - pos is -1 or a valid index
#
# Follow up: Can you solve it using O(1) extra memory?  (Yes: Floyd's Tortoise and Hare)
#
# Time complexity: O(n)
# Space complexity: O(1)

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head == fast:         
                return True
        return False


# -----------------------------
# Helpers per i test
# -----------------------------
def build_linked_list_with_cycle(values: List[int], pos: int) -> Optional[ListNode]:
    """Crea una lista da `values` e, se pos >= 0, collega la coda al nodo di indice `pos` (0-index)."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]
    return nodes[0]

def break_cycle_if_any(head: Optional[ListNode], limit: int = 20000) -> None:
    """Utility solo per sicurezza nei test locali: percorre fino a `limit` passi e prova a spezzare eventuale ciclo."""
    # Non necessaria su LeetCode, utile per evitare loop infiniti in ambienti custom.
    seen = set()
    steps = 0
    prev = None
    curr = head
    while curr and steps < limit:
        if id(curr) in seen:
            if prev:
                prev.next = None
            return
        seen.add(id(curr))
        prev = curr
        curr = curr.next
        steps += 1


# -----------------------------
# Test cases
# -----------------------------
def test_linked_list_cycle():
    print("Running test cases for Linked List Cycle...")

    sol = Solution()

    # Example 1
    head = build_linked_list_with_cycle([3,2,0,-4], pos=1)
    assert sol.hasCycle(head) is True, "Test 1 failed"

    # Example 2
    head = build_linked_list_with_cycle([1,2], pos=0)
    assert sol.hasCycle(head) is True, "Test 2 failed"

    # Example 3
    head = build_linked_list_with_cycle([1], pos=-1)
    assert sol.hasCycle(head) is False, "Test 3 failed"

    # Extra: lista vuota
    head = build_linked_list_with_cycle([], pos=-1)
    assert sol.hasCycle(head) is False, "Test 4 failed"

    # Extra: lista senza ciclo
    head = build_linked_list_with_cycle([1,2,3,4,5], pos=-1)
    assert sol.hasCycle(head) is False, "Test 5 failed"

    # Extra: ciclo che parte dal nodo centrale
    head = build_linked_list_with_cycle([7,7,7,7,7], pos=2)
    assert sol.hasCycle(head) is True, "Test 6 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_linked_list_cycle()
