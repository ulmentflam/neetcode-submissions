class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        We need to find the maximum proffit we can find between any two prices. On one
        day we can buy, and the next we can sell but we can only do this once.

        Let's run through an example. I'm going to make a very simple 1 hot example.

        [0, 0, 1, 0, 1, 2]
        
        In this example it's very clear we want to buy either on index 2 and sell on index 5.
        In this case we buy at 2 and sell at 5 we will make a profit of 2.

        The brute force way of doing this is O(p^2) where p is the magnitude of prices.
        We will start at the 0th index and check it against the 1st, 2nd so on and get the maximum profit
        we can make at that index. Then we proceed to the next and find the maximum profit we can make at that index
        and continue until we exaust the list and take the final maximum. 

        We can optimize better. This should be doable in linear time O(p) and constant memory space.

        The way we can do that by keeping track of the lowest price we've seen so far and the best profit
        we have seen so far. 

        As we scan the prices we keep track of the lowest price we've seen at that position, and the best (max) price we've seen. 

        This is a classic DP problem. We can do it in O(1) space, because we don't need to keep track of any
        array of pointers and have only two actions. If we did this problem with more actions we would require tracking more info.
        """

        buy_price: int = prices[0] # Buy price is the lowest price we've seen so far
        max_profit: int = 0

        for p in prices:
            max_profit, buy_price = max(max_profit, p - buy_price), min(p, buy_price) # max_profit, p - buy_price is the recursive step, where we are looking back at accumulated maximizations
        
        return max_profit



        