class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        ans = 0
        count = 0
        for n in setNums:
            if (n-1) not in setNums:
                count = 1
                while n+count in setNums:
                    count += 1
            else:
                continue
            ans = max(ans,count)
        return ans