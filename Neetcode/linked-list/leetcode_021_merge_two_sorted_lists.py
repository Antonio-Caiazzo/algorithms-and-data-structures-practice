# LeetCode 21 - Merge Two Sorted Lists (Easy)
#
# Merge two sorted singly linked lists (list1, list2) into one sorted list
# by splicing together existing nodes. Return the head of the merged list.
#
# Examples:
# Input: list1 = [1,2,4], list2 = [1,3,4] -> Output: [1,1,2,3,4,4]
# Input: list1 = [], list2 = []           -> Output: []
# Input: list1 = [], list2 = [0]          -> Output: [0]
#
# Constraints:
# - Number of nodes in each list: [0, 50]
# - -100 <= Node.val <= 100
# - Both lists are sorted in non-decreasing order
#
# Time complexity:  O(n + m)  
# Space complexity: O(1)      

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        a, b = list1, list2

        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        return dummy.next


# ---------- Test Utilities ----------
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    head = ListNode()  # dummy
    tail = head
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return head.next


def to_list(head: Optional[ListNode]) -> List[int]:
    out: List[int] = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


# ---------- Tests ----------
def test_merge_two_sorted_lists():
    sol = Solution()

    # Given examples
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])
    assert to_list(sol.mergeTwoLists(l1, l2)) == [1, 1, 2, 3, 4, 4]

    assert to_list(sol.mergeTwoLists(build_linked_list([]), build_linked_list([]))) == []
    assert to_list(sol.mergeTwoLists(build_linked_list([]), build_linked_list([0]))) == [0]

    # Extra cases
    assert to_list(sol.mergeTwoLists(build_linked_list([1, 1, 1]), build_linked_list([1, 1]))) == [1, 1, 1, 1, 1]
    assert to_list(sol.mergeTwoLists(build_linked_list([-3, -1, 2]), build_linked_list([-2, 0, 3]))) == [-3, -2, -1, 0, 2, 3]
    assert to_list(sol.mergeTwoLists(build_linked_list([5, 6, 7]), build_linked_list([1, 2, 3, 4, 8]))) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert to_list(sol.mergeTwoLists(build_linked_list([1]), build_linked_list([]))) == [1]
    assert to_list(sol.mergeTwoLists(build_linked_list([]), build_linked_list([1]))) == [1]

    print("All test cases passed!")


if __name__ == "__main__":
    test_merge_two_sorted_lists()
