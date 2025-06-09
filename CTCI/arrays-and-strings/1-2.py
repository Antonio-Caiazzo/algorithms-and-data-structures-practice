# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
# Time complexity: O(n)
# Space complexity: O(1)
def check_permutation(s: str, t: str) -> bool:
    
    if(len(s) != len(t)):
        return False
    
    counts = [0] * 128
    for char in s:
        counts[ord(char)] += 1
    for char in t:
        counts[ord(char)] -=1
        if counts[ord(char)] < 0:
            return False
    return True
print(check_permutation("hello", "world"))       # False
print(check_permutation("world", "dlorw"))       # True