class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        H = defaultdict(int)
        slen = len(s)
        tlen = len(t)
        if slen != tlen:
            return False
        for n in range(slen):
            H[s[n]] += 1
            H[t[n]] -= 1

        for n in range(slen):
            if H[s[n]] != 0:
                return False
        return True
        