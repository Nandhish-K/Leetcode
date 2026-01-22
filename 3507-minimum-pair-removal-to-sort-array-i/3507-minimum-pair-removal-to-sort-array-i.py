from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(nums) :
            for i in range(1,len(nums)) :
                if nums[i] < nums[i-1] :
                    return False
            return True
        if is_sorted(nums) :
            return 0
        count = 0
        
        while True:
            minimum = float("inf")
            index = -1

            for i in range(1, len(nums)):
                pair_sum = nums[i - 1] + nums[i]
                if pair_sum < minimum:
                    minimum = pair_sum
                    index = i

            count += 1
            array = []
            i = 0

            while i < len(nums):
                if i == index - 1:
                    array.append(minimum)
                    i += 2
                else:
                    array.append(nums[i])
                    i += 1

            if is_sorted(array) :
                return count
            nums = array
