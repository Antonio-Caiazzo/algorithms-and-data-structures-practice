# LeetCode 206 - Reverse Linked List (Easy)
#
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Examples:
# Input:  head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Input:  head = [1,2]
# Output: [2,1]
#
# Input:  head = []
# Output: []
#
# Constraints:
# - The number of nodes in the list is in the range [0, 5000]
# - -5000 <= Node.val <= 5000
#
# Follow up: Reverse iteratively or recursively.
#
# Time complexity: O(n)
# Space complexity:
# - Iterative: O(1)
# - Recursive: O(n) stack depth

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    # Iterative version
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    # Recursive version
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseListRecursive(head.next)
            head.next.next = head
        head.next = None
        return newHead


# -----------------------------
# Helpers per i test
# -----------------------------
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """Crea una lista concatenata da una lista Python."""
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Converte una lista concatenata in una lista Python."""
    out: List[int] = []
    curr = head
    while curr:
        out.append(curr.val)
        curr = curr.next
    return out


# -----------------------------
# Test cases for Reverse Linked List
# -----------------------------
def test_reverse_linked_list():
    print("Running test cases for Reverse Linked List...")
    sol = Solution()

    # Example 1
    head = build_linked_list([1,2,3,4,5])
    rev = sol.reverseListIterative(head)
    assert linked_list_to_list(rev) == [5,4,3,2,1], "Test 1 failed (iterative)"

    head = build_linked_list([1,2,3,4,5])
    rev = sol.reverseListRecursive(head)
    assert linked_list_to_list(rev) == [5,4,3,2,1], "Test 1 failed (recursive)"

    # Example 2
    head = build_linked_list([1,2])
    rev = sol.reverseListIterative(head)
    assert linked_list_to_list(rev) == [2,1], "Test 2 failed (iterative)"

    head = build_linked_list([1,2])
    rev = sol.reverseListRecursive(head)
    assert linked_list_to_list(rev) == [2,1], "Test 2 failed (recursive)"

    # Example 3 (empty)
    head = build_linked_list([])
    rev = sol.reverseListIterative(head)
    assert linked_list_to_list(rev) == [], "Test 3 failed (iterative)"

    head = build_linked_list([])
    rev = sol.reverseListRecursive(head)
    assert linked_list_to_list(rev) == [], "Test 3 failed (recursive)"

    # Extra: single element
    head = build_linked_list([42])
    rev = sol.reverseListIterative(head)
    assert linked_list_to_list(rev) == [42], "Test 4 failed (iterative)"

    head = build_linked_list([42])
    rev = sol.reverseListRecursive(head)
    assert linked_list_to_list(rev) == [42], "Test 4 failed (recursive)"

    print("All test cases passed!")


if __name__ == "__main__":
    test_reverse_linked_list()
