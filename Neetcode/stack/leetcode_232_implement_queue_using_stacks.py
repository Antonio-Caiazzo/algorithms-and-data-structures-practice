# LeetCode 232 - Implement Queue using Stacks (Easy)
#
# Implement a FIFO queue using two stacks:
# - push(x): push element x to the back of the queue
# - pop(): remove and return the element from the front of the queue
# - peek(): return the front element
# - empty(): return True if the queue is empty, else False
#
# Amortized time complexity: O(1) per operation
# Space complexity: O(n)
#
# Example 1:
# Input:  ["MyQueue", "push", "push", "peek", "pop", "empty"]
#         [[], [1], [2], [], [], []]
# Output: [null, null, null, 1, 1, false]
#
# Explanation:
# MyQueue myQueue = new MyQueue();
# myQueue.push(1);    // queue is [1]
# myQueue.push(2);    // queue is [1, 2] (1 è il front)
# myQueue.peek();     // return 1
# myQueue.pop();      // return 1, queue is [2]
# myQueue.empty();    // return false

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2)) == 0
        


# Test cases for Implement Queue using Stacks
def test_my_queue():
    print("Running test cases for Implement Queue using Stacks...")
    q = MyQueue()

    # Case 1: empty at start
    assert q.empty() is True, "Test 1 failed"

    # Case 2: basic push/peek/pop
    q.push(1)
    q.push(2)
    assert q.peek() == 1, "Test 2 failed"
    assert q.pop() == 1, "Test 3 failed"
    assert q.empty() is False, "Test 4 failed"

    # Case 3: sequence with more pushes
    q.push(3)
    assert q.pop() == 2, "Test 5 failed"
    assert q.peek() == 3, "Test 6 failed"
    assert q.pop() == 3, "Test 7 failed"
    assert q.empty() is True, "Test 8 failed"

    # Case 4: more coverage
    q.push(10)
    q.push(20)
    q.push(30)
    assert q.peek() == 10, "Test 9 failed"
    assert q.pop() == 10, "Test 10 failed"
    assert q.pop() == 20, "Test 11 failed"
    assert q.peek() == 30, "Test 12 failed"
    assert q.pop() == 30, "Test 13 failed"
    assert q.empty() is True, "Test 14 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_my_queue()
