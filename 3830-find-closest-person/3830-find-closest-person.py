class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff1 = abs(z-x)
        diff2 = abs(z-y)
        if diff1 == diff2:
            return 0
        m = min(diff1,diff2)
        if m == diff1:
            return 1
        elif m == diff2:
            return 2
        