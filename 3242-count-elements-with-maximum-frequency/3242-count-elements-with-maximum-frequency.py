class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        count = 0
        m = max(list(freq.values()))
        for k in freq :
            if freq[k] == m :
                count += freq[k]
        return count