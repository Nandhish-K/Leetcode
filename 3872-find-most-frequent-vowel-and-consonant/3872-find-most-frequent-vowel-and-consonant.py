class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = Counter(s)
        vowels = {"a","e","i","o","u"}
        vowel_freq = 0
        consonant_freq = 0
        for k in freq :
            if k in vowels :
                if freq[k] > vowel_freq :
                    vowel_freq = freq[k]
            else:
                if freq[k] > consonant_freq :
                    consonant_freq = freq[k]
        return vowel_freq + consonant_freq