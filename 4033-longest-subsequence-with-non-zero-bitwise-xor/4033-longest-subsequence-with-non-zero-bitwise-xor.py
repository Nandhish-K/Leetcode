class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if 0 in nums and len(set(nums)) == 1 :
            return 0
        xor_sum = nums[0]
        for num in nums[1:] :
            xor_sum ^= num
        if xor_sum == 0 :
            return len(nums) - 1
        if xor_sum > 0 :
            return len(nums)
        