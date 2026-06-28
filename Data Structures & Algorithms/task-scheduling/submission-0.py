import heapq as h
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) # O(n)
        
        max_heap = [-c for c in count.values()]
        h.heapify(max_heap)

        time = 0
        q = deque() # Pairs of (count, idle_time)
        while max_heap or q:
            time += 1
            if not max_heap:
                time = q[0][1]
            else:
                count = 1 + h.heappop(max_heap)
                if count:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                h.heappush(max_heap, q.popleft()[0])
        
        return time
            
        