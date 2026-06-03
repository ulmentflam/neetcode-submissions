class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        The brute force and obvious way of solving this problem is with sorting. 

        This solution is O(n log(n)) where n is the magnitued of the nums.

        let's work with a smaller problem.

        [100, 4, 200, 1, 2, 3]

        we can see this list of numbers can be broken in to 3 sequences

        1, 2, 3, 4 -> len 4 (Longest)

        100 -> len 1

        200 -> len 1

        How do we know how to classify each of the above sequenes?

        Check if the value is a root of a sequence. To know if the value is a root we can check if it has a parent in the list.
        
        this means we should turn the list into a set, O(N) where N is the nums

        """

        set_nums: set = set(nums)

        longest_sequence: int = 0

        for n in nums:
            if n - 1 in set_nums:
                continue
            run: int = 0 
            while n + run in set_nums:
                run += 1
            if run > longest_sequence:
                longest_sequence = run 

        return longest_sequence