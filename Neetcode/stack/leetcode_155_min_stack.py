# LeetCode 155 - Min Stack (Medium)
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class with the following operations:
# - MinStack() initializes the stack object.
# - void push(int val) pushes the element val onto the stack.
# - void pop() removes the element on the top of the stack.
# - int top() gets the top element of the stack.
# - int getMin() retrieves the minimum element in the stack.
#
# Each operation must run in O(1) time.
#
# Example:
# Input:
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output:
# [null,null,null,null,-3,null,0,-2]
#
# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
# Time complexity: O(1) per operation
# Space complexity: O(n)

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Test cases for MinStack
def test_min_stack():
    print("Running test cases for MinStack...")
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)

    assert min_stack.getMin() == -3, "Expected getMin to be -3"
    min_stack.pop()
    assert min_stack.top() == 0, "Expected top to be 0"
    assert min_stack.getMin() == -2, "Expected getMin to be -2"
    print("All test cases passed!")


if __name__ == "__main__":
    test_min_stack()
