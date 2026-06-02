class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and a target, return the indecies (i and j) such that 
        nums[i] + nums[j] == target and i != j

        You can assume every input has one pair of indicies such that i and j statusfy the condition.

        Return in order of smallest index to largest the target pair.

        Assuming I can return the first pair that finds the target. 

        We can iterate over all the numbers and in a map, store the difference between the current number, and the target,
        with an associated index. For example:

            i = 10
            map[dif(target - num)] = i
        
        then as we iterate if we pull the number from the list, then we return the current index and the prev stored in the map.

        In worst case complexity this would look like O(nums - 1) which asymptotically is approximatly O(nums).
        Worst case would be there's no target in the list, the constraint of this problem says there will be, but still if the target is
        only satusfied by the first and last number in a large list, it will asymptotically be O(nums)
        """

        diff_idx: dict = {}
        for j, num in enumerate(nums):
            i = diff_idx.get(num, None)
            if i is not None:
                return [i, j]
            diff_idx[target - num] = j
        return []