# LeetCode 242 - Valid Anagram (Easy)
# 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Time complexity: O(n log n)
# Space complexity: O(n)
def isAnagram(s: str, t: str) -> bool:    
    if len(t) != len(s):
        return False
    return sorted(s) == sorted(t)

# Test
print(isAnagram("anagram", "nagaram"))  # Output: True
print(isAnagram("rat", "car"))          # Output: False
print(isAnagram("", ""))                # Output: True
print(isAnagram("a", "a"))              # Output: True
print(isAnagram("ab", "ba"))            # Output: True
print(isAnagram("ab", "abc"))           # Output: False
print(isAnagram("a"*10000, "a"*9999 + "b"))  # Output: False


# Time complexity: O(n)
# Space complexity: O(n)
from collections import Counter
def isAnagram(s: str, t: str) -> bool:    
    return Counter(s) == Counter(t)

# Test
print(isAnagram("anagram", "nagaram"))  # Output: True
print(isAnagram("rat", "car"))          # Output: False
print(isAnagram("", ""))                # Output: True
print(isAnagram("a", "a"))              # Output: True
print(isAnagram("ab", "ba"))            # Output: True
print(isAnagram("ab", "abc"))           # Output: False
print(isAnagram("a"*10000, "a"*9999 + "b"))  # Output: False


# Time complexity: O(n)
# Space complexity: O(n)
def isAnagram(s: str, t: str) -> bool:  
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    return True

# Test
print(isAnagram("anagram", "nagaram"))  # Output: True
print(isAnagram("rat", "car"))          # Output: False
print(isAnagram("", ""))                # Output: True
print(isAnagram("a", "a"))              # Output: True
print(isAnagram("ab", "ba"))            # Output: True
print(isAnagram("ab", "abc"))           # Output: False
print(isAnagram("a"*10000, "a"*9999 + "b"))  # Output: False