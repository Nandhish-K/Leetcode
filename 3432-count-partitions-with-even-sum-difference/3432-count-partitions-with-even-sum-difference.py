class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        for i in range(1,len(nums)) :
            left = sum(nums[0:i])
            right = sum(nums[i:])
            if abs(right - left) % 2 == 0 :
                count += 1
        return count