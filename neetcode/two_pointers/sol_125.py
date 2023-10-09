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

def isPalindrome(self, s: str) -> bool:
    def isalphanum(c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    i , j = 0 , len(s) - 1
    while i < j:
        while i < j and not isalphanum(s[i]):
            i += 1
        while j > i and not isalphanum(s[j]):
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1

    return True
