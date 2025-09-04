# LeetCode 394 - Decode String (Medium)
#
# Given an encoded string s, return its decoded string.
# Encoding rule: k[encoded_string], where the encoded_string is repeated exactly k times.
#
# Examples:
# Input:  s = "3[a]2[bc]"
# Output: "aaabcbc"
#
# Input:  s = "3[a2[c]]"
# Output: "accaccacc"
#
# Input:  s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
#
# Constraints:
# - 1 <= s.length <= 30
# - s consists of lowercase English letters, digits, and square brackets '[]'
# - Input is guaranteed valid; all integers in s are in [1, 300]
#
# Time complexity: O(n + N^2)
# Space complexity: O(n + N)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                # prendi la stringa interna fino alla '['
                decoded_string = ""
                while stack and stack[-1] != "[":
                    decoded_string = stack.pop() + decoded_string
                stack.pop()  # rimuovi '['

                # calcola il moltiplicatore k (possibili più cifre)
                k = 0
                m = 1
                while stack and stack[-1].isdigit():
                    k = m * int(stack.pop()) + k
                    m *= 10

                # spingi la stringa ripetuta
                stack.append(k * decoded_string)

        return "".join(stack)


# -----------------------------
# Test cases for Decode String
# -----------------------------
def test_decode_string():
    print("Running test cases for Decode String...")
    sol = Solution()

    # Esempi ufficiali
    assert sol.decodeString("3[a]2[bc]") == "aaabcbc", "Test 1 failed"
    assert sol.decodeString("3[a2[c]]") == "accaccacc", "Test 2 failed"
    assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef", "Test 3 failed"

    # Casi aggiuntivi
    assert sol.decodeString("10[a]") == "aaaaaaaaaa", "Test 4 failed"
    assert sol.decodeString("abc3[cd]xyz") == "abccdcdcdxyz", "Test 5 failed"
    assert sol.decodeString("2[ab3[c]]") == "abcccabccc", "Test 6 failed"
    assert sol.decodeString("a") == "a", "Test 7 failed"
    assert sol.decodeString("1[a]") == "a", "Test 8 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_decode_string()
