class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        
        intervals.sort(key=lambda x: x[0])
        
       
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
           
            if merged[-1][1] >= intervals[i][0]:
                
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                
                merged.append(intervals[i])
        
        return merged


        