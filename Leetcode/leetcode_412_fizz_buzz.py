# LeetCode 412 - Fizz Buzz (Easy)
#
# Given an integer n, return a string array answer (1-indexed) where:
# - answer[i] == "FizzBuzz" if i is divisible by 3 and 5
# - answer[i] == "Fizz" if i is divisible by 3
# - answer[i] == "Buzz" if i is divisible by 5
# - answer[i] == i (as a string) otherwise
#
# Example:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
#
# Time complexity: O(n)
# Space complexity: O(n) for the output list

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result


# Test cases for FizzBuzz
def test_fizz_buzz():
    print("Running test cases for FizzBuzz...")
    sol = Solution()
    assert sol.fizzBuzz(3) == ["1","2","Fizz"], "Test case 1 failed"
    assert sol.fizzBuzz(5) == ["1","2","Fizz","4","Buzz"], "Test case 2 failed"
    assert sol.fizzBuzz(15) == [
        "1","2","Fizz","4","Buzz",
        "Fizz","7","8","Fizz","Buzz",
        "11","Fizz","13","14","FizzBuzz"
    ], "Test case 3 failed"
    print("All test cases passed!")


if __name__ == "__main__":
    test_fizz_buzz()
