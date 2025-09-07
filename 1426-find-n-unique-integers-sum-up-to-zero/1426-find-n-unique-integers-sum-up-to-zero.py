class Solution:
    def sumZero(self, n: int) -> List[int]:
        # res = []
        # if not n%2 :
        #     half = n//2
        #     for i in range(-half,half+1,1):
        #         if i!=0:
        #             res.append(i)
        # else:
            
        #     half = n//2
        #     for i in range(-half,half+1,1):
        #         res.append(i)
        # return res
        return [n*(1-n)//2] + list(range(1,n))
