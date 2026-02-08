class Solution:
    def checkString(self, s: str) -> bool:
        # return s == "".join(sorted(s))
        for i in range(1,len(s)) :
            if s[i] < s[i-1] :
                return False
        return True