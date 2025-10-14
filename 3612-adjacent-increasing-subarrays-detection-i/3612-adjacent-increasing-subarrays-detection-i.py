class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n - 2 * k + 1):
            arr1 = nums[i:i+k]
            arr2 = nums[i+k:i+2*k]
            
            if self.isStrictlyIncreasing(arr1) and self.isStrictlyIncreasing(arr2):
                return True
        return False

    def isStrictlyIncreasing(self, arr):
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True
