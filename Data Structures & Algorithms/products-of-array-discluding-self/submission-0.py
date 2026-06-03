class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Every number at an index is the product of all the previous numbers, and next numbers.

        The simplest way to solve this would be to multiply all the numbers, then at each index devide by the number excluded.

        [1, 2, 4, 6] = prod([1, 2, 4, 6]) = 48
        [48/1, 48/2, 48/4, 48/6]

        This is in O(n) where n is the magnitude of the numbers time complexity and O(1) space.

        However we might be able to get linear time with an alternative method.

        [1, 2, 4, 6]

        The multiplications at each posision are as follows 
        [2*4*6, 1*4*6, 1*2*6, 1*2*4]

        We would like to make an O(n) pass.

        We can do a forward and backward pass like algorithm.
        We store the multiplications up to the last index, the work backwards in a single loop
        haveing stored the forward products.

        In python there might be a trick we can use because there's a negative index, but let's skip this.
        """

        n = len(nums)
        forward_prods: list[int] = [1] * n
        backward_prods: list[int] = [1] * n

        for i in range(1, n):
            forward_prods[i] = nums[i - 1] * forward_prods[i - 1]
        for i in range(n - 2, -1, -1):
            backward_prods[i] = nums[i + 1] * backward_prods[i + 1]
        for i in range(n):
            nums[i] = forward_prods[i] * backward_prods[i]
        return nums


        