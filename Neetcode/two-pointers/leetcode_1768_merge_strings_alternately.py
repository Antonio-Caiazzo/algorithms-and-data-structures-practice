# LeetCode 1768 - Merge Strings Alternately (Easy)
#
# You are given two strings, word1 and word2.
# Merge the strings by alternating letters from each word, starting with word1.
# If one string is longer than the other, append the remaining letters at the end.
#
# Example 1:
# Input:  word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
#
# Example 2:
# Input:  word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
#
# Example 3:
# Input:  word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
#
# Constraints:
# - 1 <= word1.length, word2.length <= 100
# - word1 and word2 consist of lowercase English letters
#
# Time complexity: O(n)
# Space complexity: O(n), for the result string

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        merge_str = []

        while l < len(word1) and r < len(word2):
            merge_str.append(word1[l])
            merge_str.append(word2[r])
            l += 1
            r += 1
        merge_str.append(word1[l:])
        merge_str.append(word2[r:])
        return "".join(merge_str)

# Test
def test_merge_alternately():
    s = Solution()

    w1 = "abc"
    w2 = "pqr"
    print(s.mergeAlternately(w1, w2))  # Output: "apbqcr"

    w3 = "ab"
    w4 = "pqrs"
    print(s.mergeAlternately(w3, w4))  # Output: "apbqrs"

    w5 = "abcd"
    w6 = "pq"
    print(s.mergeAlternately(w5, w6))  # Output: "apbqcd"

    w7 = "a"
    w8 = "z"
    print(s.mergeAlternately(w7, w8))  # Output: "az"

    w9 = "hello"
    w10 = ""
    print(s.mergeAlternately(w9, w10))  # Output: "hello"

test_merge_alternately()
