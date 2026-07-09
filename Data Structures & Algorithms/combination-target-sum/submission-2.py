class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []

        nums.sort()

        def dfs(idx: int, sums: List[int], t: int):
            if t == target:
                res.append(sums.copy())
                return

            for i in range(idx, len(nums)):
                n = t + nums[i]
                if n > target:
                    return
                sums.append(nums[i])
                dfs(i, sums, n)
                sums.pop()
    
        dfs(0, [], 0)
        return res


                
                