class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        first = True
        count = 0
        
        for i in nums:
            if i == 1:
                if not first and count < k:
                    return False
                first = False
                count = 0
            else:
                if not first:
                    count += 1
        return True
