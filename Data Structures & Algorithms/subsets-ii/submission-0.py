class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        nums.sort() # Sort O(n log n) pales in comparison to O(n * 2^n)

        subset: List[int] = []
        def dfs(idx: int):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            
            root: int = nums[idx]
            subset.append(root)
            dfs(idx+1)
            subset.pop()
            
            # Don't search already found subset items (prevents it's root from being added but doesn't stop it's participation.)
            while (idx + 1) < len(nums) and root == nums[idx+1]:
                idx += 1 
            dfs(idx+1)
        
        dfs(0)
        return res
            
        