class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        p = 1
        for i in range(len(nums)-1):
            p *= nums[i]
            ans[i+1] *= p
            #print(i)
        #print(ans)
        p = 1
        for i in range(len(nums)-1,0,-1):
            p *= nums[i]
            ans[i-1] *= p
        #print(ans)
        return ans


