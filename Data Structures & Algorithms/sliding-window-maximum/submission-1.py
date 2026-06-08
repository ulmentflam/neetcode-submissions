class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        I believe we can do this in O(N) where n is the size of nums space.

        This is very similar to a convolution and basically is a moving average.
        
        The brute force is basically doing the following.
        res = []
        for l in range(0, len(nums), k):
            res.append(max(nums[l : l + k])) # This is of complexity O(N * K) where N is the nums, and K is the number of k

        More optimal in time complexity, we can do a version of this with dynamic programming.
        Our dp list will keep the maximum prefix. As we move the window, adding an element and
        removing an element, we will update 
        """
        return [max(nums[l : l + k]) for l in range((len(nums) + 1 - k))]
            