class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring. 

        First thing I think about is finding all the substrings of s. 

        This I believe has combinatorial time complxity. So I know we can do better.

        From each position we should keep track of the longest substring we've seen so far.

        There's a few variables I believe we need to track.

        What's the current longest substring at this position. 

        Are we currently traversing the characters in this substring, (duplicated substring).

        A sub-string should have a fixed order, meaning that it's not a palendrome (xyz is not the same as zyx) in terms of a substring.
        """

        idx_map: dict = {}
        left: int = 0
        len_longest: int = 0

        # The left pointer tracks first index of the longest substring we've seen so far. 
        # The right pointer keeps track of the current character we are viewing in the list.
        # If we've seen the right character before (previously in the list), we shift the window
        # to the largest pointer we've seen so far. This way the window increases in size, but we
        # keep sliding it along at the maximum lenght we've seen of substring so far. 
        # We leverage the map, because when we see a duplicate character, we can jump to that point.
        for right in range(len(s)):
            c = s[right]
            if c in idx_map:
                idx = idx_map[c]
                # We look for the maximum of the next left index and the current
                left = max(idx + 1, left)
            idx_map[c] = right
            len_longest = max(len_longest, (right - left) + 1)
        return len_longest

    

            

        