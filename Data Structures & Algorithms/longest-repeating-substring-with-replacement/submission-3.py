class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        We should track the longest substring, if we make at MOST k replacments.

        This has a similar behavior to the longest substring, except we have a pre-seeded k value.

        We can use our fast and slow pointers to scan the list and check ahead a particular number
        in the substring to see if we can extend it by K and get a longer sequence for the window.
        
        """

        count: dict[str, int] = {}
        results: int = 0

        r: int
        l: int = 0
        max_frq: int = 0
        for r in range(len(s)):
            c = s[r]
            count[c] = 1 + count.get(c, 0)
            max_frq = max(max_frq, count[c])
            
            # Forward checks if the next k positions in the 
            # sliding window would exceed the max_frq.
            # If so we adjust the size of our window accordingly.
            # Decrementing the character with the lesser count to the current 
            # maximum lenght and shifting our slow pointer one (popping off the lesser pointer)
            while ((r - l + 1) - max_frq) > k:
                count[s[l]] -= 1
                l += 1
            results = max(results, (r - l + 1))
        return results


        