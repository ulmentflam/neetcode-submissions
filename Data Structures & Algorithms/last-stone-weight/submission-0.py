import heapq as h

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        h.heapify(max_heap)
        while len(max_heap) >= 2:
            y = -h.heappop(max_heap)
            x = -h.heappop(max_heap)
            if x == y:
                continue
            if x < y:
                h.heappush(max_heap, -(y-x))
        return -max_heap[0] if max_heap else 0
