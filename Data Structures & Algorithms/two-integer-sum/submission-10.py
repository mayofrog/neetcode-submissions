class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        H = {}
        for i, n in enumerate(nums):
            a = target - n
            if(a in H):
                return [H[a], i]
            H[n] = i
        return [] 