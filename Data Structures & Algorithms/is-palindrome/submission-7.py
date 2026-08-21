class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for c in s:
            if c.isalnum():
                a += c.lower()
        # mid = len(a) // 2
        # return a[0:mid] == a[-1:mid:-1]
        return a == a[::-1]
