import heapq as h
class MedianFinder:

    # The median is the middle value in a sorted list
    # [1, 3, 5] median is 3
    # [1] median is 1
    # [1, 3] median is 1.5
    # Our list increases in size every time we add a number.
    # The easy way to solve this is to maintain a sorted list.
    # The naieve variation would be O(nlogn) where we sort the list each time.
    # We can do this nicely with a heep. 
    # That would give us O(log n) insertion, but O(n/2) or O(n) pops to find the median.
    # The clever way of doing this is with two heaps. We must keep the heaps sudo balanced.
    # Adding or removing an element is O(log n)
    # Finding the max is O(1), finding the min is also O(1).
    small: list[int] # Max heap
    large: list[int] # Min heap

    def __init__(self):
        self.small = []
        self.large = []
        h.heapify(self.small)
        h.heapify(self.large)

    def addNum(self, num: int) -> None:
        h.heappush(self.small, -num)

        if (self.small and self.large and -self.small[0] > self.large[0]):
            n = -h.heappop(self.small)
            h.heappush(self.large, n)
        
        if len(self.small) > len(self.large) + 1:
            n = -h.heappop(self.small)
            h.heappush(self.large, n)

        if len(self.large) > len(self.small) + 1:
            n = -h.heappop(self.large)
            h.heappush(self.small, n)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2

        
        