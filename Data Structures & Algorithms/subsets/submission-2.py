class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n: int = len(nums)
        results: List[List[int]] = []
        subset: List[int] = []
        
        def dfs(idx: int):
            if idx >= n:
                results.append(subset.copy()) # Must copy the subset so it's frozen before additional mutation.
                return
            subset.append(nums[idx]) # Add this number.
            dfs(idx + 1) # Decision to include this number, looking at the left subtree.

            subset.pop() # Don't include this element.
            dfs(idx + 1) # Look at the right subtree.
        
        dfs(0) # Increments until the end.
        return results