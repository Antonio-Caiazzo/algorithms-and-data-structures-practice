# LeetCode 225 - Implement Stack using Queues (Easy)
#
# Implement a LIFO stack using queue operations only:
# - push(x): push element x onto stack
# - pop(): remove and return the element on top of the stack
# - top(): return the element on top of the stack
# - empty(): return True if stack is empty, else False
#
# This solution uses a SINGLE queue (follow-up) and rotates elements on pop.
#
# Time complexity:
# - push:  O(1)
# - pop:   O(n) 
# - top:   O(1)
# - empty: O(1)
#
# Space complexity: O(n)

from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


# -----------------------------
# Test cases for MyStack
# -----------------------------
def test_my_stack():
    print("Running test cases for Implement Stack using Queues...")
    s = MyStack()
    assert s.empty() is True, "Test 1 failed"

    s.push(1)
    s.push(2)
    assert s.top() == 2, "Test 2 failed"
    assert s.pop() == 2, "Test 3 failed"
    assert s.top() == 1, "Test 4 failed"
    assert s.empty() is False, "Test 5 failed"

    s.push(3)
    s.push(4)
    assert s.pop() == 4, "Test 6 failed"
    assert s.pop() == 3, "Test 7 failed"
    assert s.pop() == 1, "Test 8 failed"
    assert s.empty() is True, "Test 9 failed"

    # Extra: push/pop alternati
    s.push(10)
    assert s.top() == 10, "Test 10 failed"
    s.push(20)
    assert s.pop() == 20, "Test 11 failed"
    assert s.pop() == 10, "Test 12 failed"
    assert s.empty() is True, "Test 13 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_my_stack()
