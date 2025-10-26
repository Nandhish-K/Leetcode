class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_in_minutes = int(current[:2]) * 60 + int(current[3:])
        correct_in_minutes = int(correct[:2]) * 60 + int(correct[3:])
        diff = correct_in_minutes - current_in_minutes
        count = 0
        if diff == 0 :
            return count
        count += diff // 60
        diff = diff % 60
        if diff == 0 :
            return count
        count += diff // 15
        diff = diff % 15
        if diff == 0 :
            return count
        count += diff // 5
        diff = diff % 5
        if diff == 0 :
            return count
        count += diff // 1
        return count
        
