class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            # if a > 0:
            #     break
            j = i+1
            k = len(nums)-1
            while(j<k):
                sum = a + nums[j] + nums[k]
                if sum == 0:
                    ans.append([a,nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1
        return ans
            