class Solution:
    def findMin(self, nums: List[int]) -> int:
        n: int = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
        