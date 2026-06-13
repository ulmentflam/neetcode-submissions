class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []

        results: List[int] = [0] * len(temperatures)
        stack: List[int] = [] # Stack stores the index of the max

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                results[idx] = i - idx
            stack.append(i)
        return results
        