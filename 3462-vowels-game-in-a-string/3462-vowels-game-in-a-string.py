class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = 0
        vowels = {"a","e","i","o","u"}
        for ch in s:
            if  ch in vowels :
                count += 1
        if count == 0:
            return False
        if count%2==1:
            return True
        if count%2==0:
            return True

        
        