class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor_sum = 0
        for n in nums :
            xor_sum ^= n
        if xor_sum != 0 :
            return len(nums)
        elif nums.count(0) == len(nums) :
            return 0
        return len(nums) - 1