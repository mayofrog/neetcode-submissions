class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False
        
        for i in range(s_len):
            d[s[i]] += 1
            d[t[i]] -= 1
        
        for i in d.values():
            if i != 0:
                return False
        return True