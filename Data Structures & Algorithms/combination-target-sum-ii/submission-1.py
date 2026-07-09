class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []
        c: int = len(candidates)
        candidates.sort()
        def dfs(idx: int, sums: List[int]):
            total = sum(sums)
            if total == target:
                res.append(sums.copy())
                return
            if idx >= c or total > target:
                return

            root = candidates[idx]
            sums.append(root)
            dfs(idx + 1, sums)
            sums.pop()
            while idx + 1 < c and root == candidates[idx + 1]:
                idx += 1
            dfs(idx + 1, sums)
        dfs(0, [])
        return res