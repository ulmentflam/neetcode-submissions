class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n: int = len(nums)
        l, r = 0, n - 1

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        pivot = l # The pivot point becomes our found idx
        l, r = 0, n - 1

        if target == nums[pivot]:
            return pivot

        if target == nums[r]:
            return r

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
        

        