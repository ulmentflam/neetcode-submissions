import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        This is top_k sampling. Given an integer list, find the frequency and sample the top_k
        elements.

        Top k can be returned in any order.

        Sampling the frequencies will be O(nums log nums) + O(k) to sample the data. The asmptotics of 
        sampling the frequencies will drown out the O(k).

        We can do this in the memory space of O(r + k) where R is the number of repeated items in nums
        
        I would like to avoid sorting, because I can keep track of top_k with a datastructure. 
        """
        frequency: dict[int, int] = {}
        top_nums: list[int] = []
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
            heapq.heappush(top_nums, (-frequency[n], n)) # O(log n)
    
        top_k: set[int] = set()
        i: int = 0
        while i < k:
            _, num = heapq.heappop(top_nums)
            if num not in top_k:
                top_k.add(num)
                i += 1
        return list(top_k) # Because the output can be in ANY order
        

        