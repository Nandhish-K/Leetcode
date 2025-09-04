class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # res = []
        # freq = Counter(nums)
        # for key in freq.keys():
        #     if freq[key] == 2:
        #         res.append(key)
        # return res
        n = len(nums)
        hashmap = [0]*(n+1)
        for i in range(n):
            hashmap[nums[i]] += 1
        
        res = []
        for j in range(1,n+1):
            if hashmap[j]>1:
                res.append(j)
        return res