class Solution:
    def sortVowels(self, s: str) -> str:
        # lower = []
        # upper = []
        # vowels = {"A","E","I","O","U","a","e","i","o","u"}
        # for ch in s:
        #     if ch.isupper() and ch in vowels:
        #         upper.append(ch)
        #     elif ch.islower() and ch in vowels:
        #         lower.append(ch)
        # upper.sort()
        # lower.sort()
        # combination = upper + lower
        # res = ""
        # i = 0
        # for ch in s:
        #     if ch not in vowels:
        #         res +=ch
        #     else:
        #         res +=combination[i]
        #         i+=1
        # return res
        vowels = {"A","E","I","O","U","a","e","i","o","u"}
        res = []
        for ch in s:
            if  ch in vowels:
                res.append(ch)
        res.sort()
        result = ""
        i = 0
        for ch in s:
            if ch in vowels:
                result += res[i]
                i += 1
            else:
                result += ch
        return result
