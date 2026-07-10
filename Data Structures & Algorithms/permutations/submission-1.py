class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l: int = len(nums)
        res: List[List[int]] = []

        def dfs(idx: int):
            if idx == l:
                res.append(nums[:])
                return
            for i in range(idx, l):
                nums[idx], nums[i] = nums[i], nums[idx] # Swap i and the current idx
                dfs(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx] # Swap back after traversing
        dfs(0)
        return res
        