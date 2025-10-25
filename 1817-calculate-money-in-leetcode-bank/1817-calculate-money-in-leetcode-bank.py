class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        monday = 1
        day = 0

        for i in range(1, n + 1):
            total += monday + (i - 1) % 7
            day += 1
            if day == 7:
                day = 0
                monday += 1
        return total
