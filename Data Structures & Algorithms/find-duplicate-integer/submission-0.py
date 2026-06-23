class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        cycle = 0
        while True:
            slow = nums[slow]
            cycle = nums[cycle]
            if slow == cycle:
                return slow
        
        