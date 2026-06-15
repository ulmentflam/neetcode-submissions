class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        while l <= r:
            pivot = (l + r) // 2 # We don't need to worry about overflow here as we are aren't searching by index

            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / pivot)
            if total_time <= h:
                k = pivot
                r = pivot - 1
            else:
                l = pivot + 1
        return k
            