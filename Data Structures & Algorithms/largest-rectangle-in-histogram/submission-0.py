class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n: int = len(heights)
        max_area: int = 0
        stack: List[Tuple[int, int]] = [] # Each point in the stack holds a index and height
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (n - i))
        return max_area


            