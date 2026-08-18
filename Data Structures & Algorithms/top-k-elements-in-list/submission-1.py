class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        H = defaultdict(int)
        for n in nums:
            H[n] += 1
        heap = []
        for a in H:
            heapq.heappush(heap, (H[a], a))
            if len(heap) > k:
                heapq.heappop(heap)
        a = []
        for i in range(k):
            a.append(heapq.heappop(heap)[1])

        return a