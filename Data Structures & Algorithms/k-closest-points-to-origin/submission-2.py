import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclidian(point: List[int]) -> float:
            assert len(point) == 2
            x,y = point
            return (x**2 + y**2) ** 0.5
        
        min_heap_distances = [ (euclidian(point), point) for point in points]
        heapq.heapify(min_heap_distances)
        results = []
        for _ in range(k):
            (dist, point) = heapq.heappop(min_heap_distances)
            results.append(point)
        return results
        