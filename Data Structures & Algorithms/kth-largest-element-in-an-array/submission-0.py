import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for n in nums:
            h.heappush(min_heap,n)
            while len(min_heap) > k:
                h.heappop(min_heap)
        return min_heap[0]