class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m: int = len(matrix)
        n: int = len(matrix[0])

        # We can do some index arithmatic to capture positions in std binary search
        l, r = 0, m * n - 1

        while l <= r:
            pivot = l + ((r - l) // 2)
            i, j = (pivot // n, pivot % n)
            if target > matrix[i][j]:
                l = pivot + 1
            elif target < matrix[i][j]:
                r = pivot - 1
            else:
                return True
        return False

        