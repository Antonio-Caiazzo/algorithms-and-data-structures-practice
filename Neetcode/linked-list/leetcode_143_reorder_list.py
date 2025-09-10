# LeetCode 143 - Reorder List (Medium)
#
# Given the head of a singly linked list L0→L1→…→Ln, reorder it in-place to:
# L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify node values; only relink nodes.
#
# Examples:
# Input: head = [1,2,3,4]   -> Output: [1,4,2,3]
# Input: head = [1,2,3,4,5] -> Output: [1,5,2,4,3]
#
# Constraints:
# - 1 <= number of nodes <= 5 * 10^4
# - 1 <= Node.val <= 1000
#
# Approach (same logic as your solution):
# 1) Find middle using slow/fast pointers (stop at node before second half).
# 2) Reverse the second half.
# 3) Merge first half and reversed second half by alternating nodes.
#
# Time complexity:  O(n)
# Space complexity: O(1)

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev:
            next_head = head.next
            next_reverse = prev.next
            head.next = prev
            prev.next = next_head
            head = next_head
            prev = next_reverse


# ---------- Test Utilities ----------
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode], cap: int = 200000) -> List[int]:
    out: List[int] = []
    cur = head
    while cur and cap:
        out.append(cur.val)
        cur = cur.next
        cap -= 1
    return out


# ---------- Tests ----------
def test_reorder_list():
    sol = Solution()

    # Given examples
    h = build_linked_list([1, 2, 3, 4])
    sol.reorderList(h)
    assert to_list(h) == [1, 4, 2, 3]

    h = build_linked_list([1, 2, 3, 4, 5])
    sol.reorderList(h)
    assert to_list(h) == [1, 5, 2, 4, 3]

    # Edge cases
    h = build_linked_list([1])
    sol.reorderList(h)
    assert to_list(h) == [1]

    h = build_linked_list([1, 2])
    sol.reorderList(h)
    assert to_list(h) == [1, 2]

    h = build_linked_list([1, 2, 3])
    sol.reorderList(h)
    assert to_list(h) == [1, 3, 2]

    # Additional
    h = build_linked_list([10, 20, 30, 40, 50, 60])
    sol.reorderList(h)
    assert to_list(h) == [10, 60, 20, 50, 30, 40]

    print("All test cases passed!")


if __name__ == "__main__":
    test_reorder_list()
