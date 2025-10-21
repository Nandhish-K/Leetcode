class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for operation in operations :
            if operation == "--X" :
                res -= 1
            elif operation == "X--" :
                res -= 1
            elif operation == "X++" :
                res += 1
            else :
                res += 1
        return res