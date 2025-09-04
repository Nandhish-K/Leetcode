class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {num: i for i, num in enumerate(nums2)}
        res = []
        for num in nums1:
            idx = d[num]
            found = -1
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > num:
                    found = nums2[j]
                    break
            res.append(found)
        return res
