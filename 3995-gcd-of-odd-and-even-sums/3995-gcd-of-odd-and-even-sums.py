class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # start = 1
        # oddsum = 0
        # evensum = 0
        # for i in range(n):
        #     oddsum += start
        #     evensum += start+1
        #     start +=2
        # return math.gcd(oddsum,evensum)
        # oddsum = n*n
        # evensum = n*(n+1)
        #gcd = gcd(n**2,n*(n+1))
        #gcd = n*gcd(n,n+1)
        #gcd = n*1
        #gcd = n
        return n