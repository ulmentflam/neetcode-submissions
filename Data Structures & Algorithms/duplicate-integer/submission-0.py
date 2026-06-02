class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        We are given an array of nums, and we want to return a boolean if ANY value
        appears more then one time.

        Here's an example:
        hasDuplicate([1, 3, 5, 7, 9, 1]) = True
        hasDuplicates([3, 5, 7, 1, 9, 13, 4, 4]) = True

        This should be do able in O(nums) time where nums is the size of the array.
        This can be done with slightly better then O(nums) space.
        """

        nums_seen: dict = {}
        # The traditional iterative method
        for n in nums:
            if nums_seen.get(n): # Dictionary Lookup O(1)
                return True
            nums_seen[n] = 1
        # Can we optimize this further? We are dealing with integers so we might be 
        # able to do some form of hashing to detect duplicates
        return False