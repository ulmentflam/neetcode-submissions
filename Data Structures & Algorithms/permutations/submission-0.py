class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l: int = len(nums)
        res: List[List[int]] = []

        def dfs(perms: List[int], picks: List[bool]):
            if len(perms) == l:
                res.append(perms.copy())
                return
            for i in range(l):
                if not picks[i]:
                    perms.append(nums[i])
                    picks[i] = True
                    dfs(perms, picks)
                    perms.pop()
                    picks[i] = False 
        dfs([], [False] * l)
        return res