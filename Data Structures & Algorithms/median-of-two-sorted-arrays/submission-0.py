class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n: int = len(nums1)
        m: int = len(nums2)

        def get_k_smallest(a: List[int], b: List[int], k: int = 0) -> int:
            if not a < b:
                b, a = a, b
            if not a:
                return b[k - 1]
            if k == 1:
                return min(a[0], b[0])
            i = min(len(a), k // 2)
            j = min(len(b), k // 2)
            if a[i - 1] <= b[j - 1]:
                return get_k_smallest(a[i:], b, k - i)
            return get_k_smallest(a, b[j:], k - j)
        
        total = m + n
        if total % 2 != 0:
            return get_k_smallest(nums1, nums2, (total + 1) // 2)
        return (get_k_smallest(nums1, nums2, total // 2) + get_k_smallest(nums1, nums2, total // 2 + 1)) / 2
            