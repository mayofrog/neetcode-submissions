class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # setA = set()
        # for n in nums:
        #     if n in setA:
        #         return False
        #     setA.add(n)
        # return True

        H = defaultdict(int)
        for n in nums:
            if H[n] == 1:
                return True
            H[n] = 1
        return False