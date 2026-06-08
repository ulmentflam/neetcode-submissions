class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        We are tasked with checking if s2 is a permutation of s1. 

        This is essentially a sliding window problem, where the window is
        fixed to the length of the string and we are checking if any string in that
        window matches as a permutation.

        The best way to check if a string in a window is a permutation is verifying that
        all the chars in the fixed window exist in the set of value counts, then returning true.
        Otherwise we should return false.
        """
        n_s1: int = len(s1)
        n_s2: int = len(s2)

        if n_s1 > n_s2:
            return False
        
        def hash_str(s: str) -> str:
            count_hot_enc: list = [0] * 26 # assuming ascii char strings, and constraint of lower case letters.
            for c in s:
                count_hot_enc[ord(c) - ord('a')] += 1
            return str(count_hot_enc)

        s1_hash = hash_str(s1)
        
        if n_s1 == n_s2:
            return s1_hash == hash_str(s2)

        l: int = 0
        
        while l + n_s1 <= n_s2:
            if hash_str(s2[l : l + n_s1]) == s1_hash:
                return True
            l += 1

        return False
