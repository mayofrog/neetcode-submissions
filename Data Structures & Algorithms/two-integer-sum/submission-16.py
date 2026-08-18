class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        H = {}
        for i,n in enumerate(nums):
            if target - n in H:
                return [H[target - n], i]
            H[n] = i
        return []