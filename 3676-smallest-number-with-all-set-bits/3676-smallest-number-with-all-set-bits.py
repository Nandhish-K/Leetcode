class Solution:
    def smallestNumber(self, n: int) -> int:
        while True :
            b = bin(n)[2:]
            freq = Counter(b)
            if "1" in b and freq["1"] == len(b) :
                return n
            n += 1