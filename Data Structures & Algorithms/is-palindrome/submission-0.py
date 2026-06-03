class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        A palindrome is the same string forward and backword.
        
        In this case our string can have any unicode characters.

        The fastest solution to this problem I setting a pointer at both the start and the end of the sequence.
        
        While we iterate we compare the left and right values untill the indecies are equal.

        This is a case of the two-pointers algorithm which is O(n)
        """
        n: int = len(s)
        left, right = 0, n - 1

        while left < right:
            if not s[right].isalnum():
                right -= 1
                continue

            if not s[left].isalnum():
                left += 1
                continue

            if s[left].lower() != s[right].lower():
                return False
                
            right -= 1
            left += 1
        return True

        