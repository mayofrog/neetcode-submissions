class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        H = {}
        for i, num in enumerate(nums):
            val = target-num
            if val in H:
                return [H[val],i]
            H[num] = i;
        return []
        