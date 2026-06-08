class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Brute force:

            for each substring (O(s^2) where s is the magnitued of the string):
                if the substring contains t and len(substring) < len(min_substring):
                    min_substring = substring
            return min_substring

        The faster method would be a dynamic sliding window. 

        We know in the worst case the minimum can't be less then the lenth of s

        We also know that for it to be valid the smallest minimum is the len(t).

        Our approach should be setting a right and left pointer. Working our way inside through substrings.        
        """
        n_s: int = len(s)
        n_t: int = len(t)

        # We can cross some edgecases out here. Lenght mismatches etc...

        min_substring: str = "" # This is the case where the string doesn't exist as a substring
        len_min: int = len(s) + 1
        
        l: int = 0
        r: int = n_s - 1

        def get_idx(c: str) -> int:
            shift: int = 2 if c.isupper() else 1
            lower_idx = ord(c.lower()) - ord('a')
            if shift == 2 and lower_idx == 0:
                return 26
            
            return (ord(c.lower()) - ord('a')) * shift 

        freq_t = [0] * 52

        for c in t:
            idx = get_idx(c)
            freq_t[idx] += 1

        freq_s = [0] * 52

        l: int = 0
        have, need = 0, n_t
        for r in range(n_s):
            idx_r = get_idx(s[r])
            freq_s[idx_r] += 1

            if freq_t[idx_r] >= freq_s[idx_r]:
                have += 1
            
            while have == need:
                if (r - l + 1) < len_min:
                    min_substring, len_min = s[l : r + 1], r - l + 1
                idx_l = get_idx(s[l])
                freq_s[idx_l] -= 1
                if freq_s[idx_l] < freq_t[idx_l]:
                    have -= 1
                l += 1
        return min_substring
            



        