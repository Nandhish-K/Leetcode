class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        res = []
        
        for num in arr:
            res.append(num)
            if num == 0:
                res.append(0)
            if len(res) >= n:
                break
        
        for i in range(n):
            arr[i] = res[i]
