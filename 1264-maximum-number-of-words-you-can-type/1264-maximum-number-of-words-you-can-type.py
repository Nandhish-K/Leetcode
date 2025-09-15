class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr = text.split(" ")
        count = 0
        for s in arr :
            flag = False
            for ch in brokenLetters :
                if ch in s :
                    flag = True
                    break 
            if not flag :
                count += 1
        return count