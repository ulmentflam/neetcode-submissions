class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        We are given the same input array as in the two sum problem.

        For this version of the problem we are looking for 3 values that sum to zero WITHOUT duplicates.

        Unlike two sum and two sum II we don't have a variable target that can be passed in.

        Also unlike two sum II the input array is not sorted, so we will most likely need to sort it..

        We are searching for 3 points a, b, c that all sum to zero. We can the way this problem can be
        broken down is into two sum II with a third dimension. The OVERALL target is a sum to 0,
        While the local target for two sum is a sum to target. (in this case a negative value). 

        So we theoritically can do this in O(n^2) time complexity where n is the numbers in the list.
        That's because we need to sort the list and replicate two sum II with at maximum 3 points.

        The reason we need to sort the list is because we must not have duplicated tripplits.

        The sorted list will give us O(m) space complexity where m is the magnitued of our nums. The sort
        itself will be of complexity nlog(n) but asmptotically get's out done by the n^2 required.
        This is very similar to tri-directional search.
        """
        
        n: int = len(nums)
        results: List[List[int]] = []    
        nums.sort() # O(nlog(n))

        def two_sum_two(idx1: int, idx2: int, target: int) -> List[tuple[int, int]]:
            res: List[tuple[int,int]] = []
            while idx1 < idx2:
                b, c = nums[idx1], nums[idx2] 
                total = b + c
                if total == target:
                    res.append((b, c))
                    idx1 += 1
                    # This is where we diverge from standard 2 sum 2
                    while idx1 < idx2 and nums[idx1] == nums[idx1 - 1]:
                        idx1 += 1
                elif total < target:
                    idx1 += 1
                else:
                    idx2 -= 1
            return res

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            b_c_pairs = two_sum_two(i + 1, n - 1, -a)
            for b,c in b_c_pairs:
                results.append([a,b,c])
        return results