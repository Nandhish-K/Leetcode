class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)-2) :
            if nums[i] + nums[i+1] > nums[i+2] and nums[i] + nums[i+2] > nums[i+1] and nums[i+1] + nums[i+2] > nums[i] :
                res = max(res,nums[i] + nums[i+1] + nums[i+2])
        return res 