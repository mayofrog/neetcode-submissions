class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i, n in enumerate(nums):
            j = target - n
            if j in d:
                return [d[j], i]
            d[n] = i
