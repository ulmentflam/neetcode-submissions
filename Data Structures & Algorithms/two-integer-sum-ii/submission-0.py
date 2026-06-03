class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        We are searching for a target int where the sum of two numbers in an array reach this target.

        This is a textbook example of the tortus and the hair algorithm.

        """
        index1: int
        index2: int
        n: int = len(numbers)
        index1, index2 = 0, n - 1 

        while index1 < n - 1:
            two_sum: int = numbers[index1] + numbers[index2]
            if two_sum == target:
                return [index1 + 1, index2 + 1]
            index2 -= 1
            if index2 == index1:
                index1, index2 = index1 + 1, n - 1
        


