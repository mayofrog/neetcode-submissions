class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        H = defaultdict(int)
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            H[s[i]] += 1
            H[t[i]] -= 1

        for i in H.values():
            if i != 0:
                return False
        return True
