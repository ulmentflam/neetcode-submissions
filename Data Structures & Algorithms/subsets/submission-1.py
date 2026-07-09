class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n: int = len(nums)
        results: List[List[int]] = []
        subset: List[int] = []
        
        def sub(idx: int):
            if idx >= n:
                results.append(subset.copy()) # Must copy the subset so it's frozen before additional mutation.
                return
            subset.append(nums[idx])
            sub(idx + 1) # Permute on the next number
            subset.pop() # Pull the last element appended to the subset
            sub(idx + 1) # Permute on the next number again (advances the iteration)
        
        sub(0) # Increments until the end
        return results