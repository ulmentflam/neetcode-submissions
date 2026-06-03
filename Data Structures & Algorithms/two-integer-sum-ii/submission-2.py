class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        We are searching for a target int where the sum of two numbers in an array reach this target.

        This is a textbook example of the tortus and the hare algorithm where we can take advantage of the array being sorted.

        We can do two pointers, where we adjust the pointers based on the proximity to the target.

        If the numbers are less then the target, then we need to move the left pointer, otherwise we need to decrease toward the target moving the right pointer.

        The compelxity of two pointers should be O(n) where n is the number of numbers

        The space complexity with two constant pointers is O(1)

        This can also be sloved with binary search, however because two numbers are involved, that would bring the complexity up to
        O(Nlog(N))

        """
        index1: int
        index2: int
        n: int = len(numbers)
        index1, index2 = 0, n - 1 

        while index1 < index2:
            total: int = numbers[index1] + numbers[index2]
            if total == target:
                return [index1 + 1, index2 + 1] # The result is 1 indexed
            elif total < target: # The numbers are sorted assending so this is like binary search.
                index1 += 1
            else:
                index2 -= 1
        raise ValueError("Target Not Found")
        
        


