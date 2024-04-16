class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap_s,  hashMap_t = {}, {}

        for char in s:
            if char in hashMap_s:
                hashMap_s[char] += 1
            else: hashMap_s[char] = 1
        for char in t:
            if char in hashMap_t:
                hashMap_t[char] += 1
            else: hashMap_t[char] = 1
        return hashMap_s == hashMap_t

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap_s, hashMap_t = {}, {}

        for i in range(len(s)):
            hashMap_s[s[i]] = 1 + hashMap_s.get(s[i], 0)
            hashMap_t[t[i]] = 1 + hashMap_t.get(t[i], 0)

        return hashMap_s == hashMap_t
