class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        H = defaultdict(int)
        for n in nums:
            if n in H:
                return True
            H[n] += 1
        return False
