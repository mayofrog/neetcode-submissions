class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        H = defaultdict(int)
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        for i in range(s_len):
            H[s[i]] += 1
            H[t[i]] -= 1
        
        for val in H.values():
            if val != 0:
                return False
        return True
