# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ""
        for c in s:
            if c.isalpha():
                print(c)
                stripped += c.lower()
            elif c.isdigit():
                stripped += c
        i, j = 0, len(stripped) - 1
        while i <= j:
            if stripped[i] != stripped[j]:
                return False
            i += 1
            j -= 1
        return True
