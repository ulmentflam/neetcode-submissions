class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Similar to two sum. We are trying to maximize the area. H x W.

        Let's start with the example and a brute force approach.

        In a brute force approach, we would go to each hight in hights. Check the area between each
        item and all of the other items. We store the maximum and do this check until we find it's maximum
        hight. Then we do the same with every item and take the Maximum of all of the max heights found.

        This would be O(H^2) in complexity where h is the heights. 

        Let's think through how I would slolve this. I would want to find the longest item and check the 
        area between it and any items as long, computing the area. Then I would look for any smaller items
        that might have a greater width. A way to do this would be to work backward from the maximum height element.

        A good way to do this would be with the two-pointers algorithm. That should be able to get us to
        O(n) complexity.

        We want to track starting at the first and last elements of the list. This would be the largest width.
        Then we work until they meet, tracking the maximum height while we go backward.
        """
        n: int = len(heights)
        l, r = 0, n - 1

        max_area: int = -1

        while l < r:
            h_l, h_r = heights[l], heights[r]
            area = min(h_l, h_r) * (r - l)
            max_area = max(max_area, area)
            if h_l > h_r:
                r -= 1
            else:
                l += 1
        return max_area