class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given an array of hights, we need to return the maximum area trapped between any two bars.

        Watter is trapped between two bars as in the picture bellow. A few constraints to think about.
        The there is a bar to "caputre" the water (hold a volume). If you look at the right of the image,
        though there are three grid spaces that can encoumpas watter, there's not a height longer then the length
        to hold the volume. The other constraint is the water volume only goes up to the smallest height.
        If you look at the left side of the image the bar on the right is taller, but the left is small.

        A brute force approach would go through each position, if there's a height, it would find the next closes value greater
        than or equal to it's value that can hold volume. Then compute the area. If there's not it would move on to the next 
        position and continue. This loop would be O(h^2) where h is the number of heights.

        We should be able to solve this in linear time O(h), using the two-pointers algorithm.
        We work forward and backward, looking for viable heights. In this case we should look for the
        maximum left and right heights. Once we hit a maximal value we should check the area between these
        values for maximality. If those values are maximul we update the max area, and continue.

        We can naturally compute the maximum as we track the left and right, this is because as the maximum moves the volume changes.
        """
        n: int = len(height)
        l, r = 0, n - 1

        l_max, r_max = height[l], height[r]
        max_volume: int = 0

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                max_volume += l_max - height[l]
            else:
                r -= 1 
                r_max = max(r_max, height[r])
                max_volume += r_max - height[r]
        return max_volume
