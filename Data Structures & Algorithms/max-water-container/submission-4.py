class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        i,j = 0,len(heights)-1
        while(i<j):
            area = min(heights[i], heights[j]) * (j-i)
            ans = max(ans, area)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return ans