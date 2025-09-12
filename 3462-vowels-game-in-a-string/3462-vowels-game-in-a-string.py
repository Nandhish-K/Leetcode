class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # count = 0
        # vowels = {"a","e","i","o","u"}
        # for ch in s:
        #     if  ch in vowels :
        #         count += 1
        # if count == 0:
        #     return False
        # if count%2==1:
        #     return True
        # if count%2==0:
        #     return True
        count = s.count('a') + s.count("e") + s.count("i") + s.count("o") + s.count("u")
        if count == 0 :
            return False
        if count %2:
            return True
        return True

        
        