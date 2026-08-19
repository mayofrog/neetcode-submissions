class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        H = defaultdict(int)
        for n in nums:
            H[n] += 1
        fre = [[] for n in range(len(nums)+1)]
        for key, value in H.items():
            fre[value].append(key)
        
        ans = []
        for i in range(len(fre)-1,0,-1):
            for n in fre[i]:
                if len(ans) < k:
                    ans.append(n)

        return ans