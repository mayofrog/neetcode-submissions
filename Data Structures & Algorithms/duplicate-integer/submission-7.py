class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        D = defaultdict(int)
        for n in nums:
            if(D[n] != 0):
                return True
            D[n] += 1
        return False
            