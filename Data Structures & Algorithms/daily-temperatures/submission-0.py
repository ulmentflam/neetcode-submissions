class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        results: List[int] = []

        for i,v in enumerate(temperatures):
            j = i
            while j < len(temperatures) and v >= temperatures[j]:
                j += 1
            if j == len(temperatures):
                results.append(0)
            else:
                results.append(j-i)
        return results




            
