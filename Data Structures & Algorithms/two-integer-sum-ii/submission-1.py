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

        while index1 < index2:
            total: int = numbers[index1] + numbers[index2]
            if total == target:
                return [index1 + 1, index2 + 1] # The result is 1 indexed
            elif total < target:
                index1 += 1
            else:
                index2 -= 1
        raise ValueError("Target Not Found")
        
        


