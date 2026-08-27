class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        pre = 1
        pos = 1
        for i,n in enumerate(nums):
            ans.append(pre)
            pre *= n
        
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= pos
            pos *= nums[i]
            
        return ans
