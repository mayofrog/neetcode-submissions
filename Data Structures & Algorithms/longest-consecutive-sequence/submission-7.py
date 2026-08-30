class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        long = 1
        count = 1
        
        for i in range(0,len(nums)):
            
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                count += 1
            else:
                count = 1
            long = max(long, count)
        if not nums:
            long = 0
        return long