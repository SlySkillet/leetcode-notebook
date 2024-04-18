class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNumeric(char):
            return(
                ord('a') <= ord(char) <= ord('z') or
                ord('A') <= ord(char) <= ord('Z') or
                ord('0') <= ord(char) <= ord('9')
            )

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not isAlphaNumeric(s[l]):
                l += 1
            while l < r and not isAlphaNumeric(s[r]):
                r -= 1
            print(s[l], s[r])
            if (s[l].lower() == s[r].lower()):
                l, r = l + 1, r - 1
            else: return False
        return True

inst = Solution()
print(inst.isPalindrome("A man, a plan, a canal: Panama"))
