from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n += 1
        while True:
            s = str(n)
            freq = Counter(s)
            if all(freq[a] == int(a) for a in freq):
                return n
            n += 1
