class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Our goal is to detect if a string is an anagram (contains the exact same chars).
        
        Given two strings a, b. We need to determine if the strings are annagrams.

        We should be able to do this in O(a) time. We can therefor just run one iteration 
        across both strings.

        We this would have the space complexity of O(a) if we create a hashmap the size of a.
        """

        # Early termination logic.
        if len(s) != len(t):
            return False
        
        char_occurances: dict = {}

        for c in s:
            if not char_occurances.get(c):
                char_occurances[c] = 0
            char_occurances[c] += 1
        
        for c in t:
            if not char_occurances.get(c):
                return False
            char_occurances[c] -= 1

        return True
            