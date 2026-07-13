class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        H = {}
        for num in nums:
            if num in H:
                return True
            H[num] = 1 
        return False


        