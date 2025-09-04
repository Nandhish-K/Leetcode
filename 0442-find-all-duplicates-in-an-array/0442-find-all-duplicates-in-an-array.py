class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        freq = Counter(nums)
        for key in freq.keys():
            if freq[key] == 2:
                res.append(key)
        return res
        