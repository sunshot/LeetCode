from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n3 = n1 + n2
        nums3 = [None] * n3
        iseven = False
        if (n3 % 2) == 0:
            iseven = True
            middle = n3/2
        else:
            middle = (n3+1)/2
        middle = middle - 1
        median = 0
        i = 0
        j = 0
        k = 0
        while i < n1 and j < n2: 
            if nums1[i] < nums2[j]:
                nums3[k] = nums1[i]
                i = i + 1
            else:
                nums3[k] = nums2[j]
                j = j + 1
            if k == middle:
                median = nums3[k]
                if not iseven:
                    return median
            if k == (middle + 1) and iseven:
                median = median + nums3[k]
                median = median / 2.0
                return median
            k = k + 1
        while i < n1:
            nums3[k] = nums1[i]
            i = i + 1
            if k == middle:
                median = nums3[k]
                if not iseven:
                    return median
            if k == middle + 1 and iseven:
                median = median + nums3[k]
                median = median / 2.0
                return median
            k = k + 1
        while j < n2:
            nums3[k] = nums2[j]
            j = j + 1
            if k == middle:
                median = nums3[k]
                if not iseven:
                    return median
            if k == middle + 1 and iseven:
                median = median + nums3[k]
                median = median / 2.0
                return median
            k = k + 1
        return median


if __name__== '__main__':
    solution = Solution()

    nums1 = [1,2]
    nums2 = [3,4]

    ans = solution.findMedianSortedArrays(nums1, nums2)
    print(ans)