class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n: int = len(temperatures)

        results: List[int] = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if results[j] == 0:
                    j = n
                    break
                j += results[j]
            if j < n:
                results[i] = j - i
        return results

        
        