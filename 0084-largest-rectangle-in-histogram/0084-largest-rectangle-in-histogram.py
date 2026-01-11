class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # def find(i) :
        #     left = i - 1
        #     right = i + 1
        #     height = heights[i]
        #     width = 1
        #     for j in range(left,-1,-1) :
        #         if heights[j] < height :
        #             break
        #         width += 1
        #     for k in range(right,len(heights),1) :
        #         if heights[k] < height :
        #             break
        #         width += 1
        #     return height*width
        # res = float("-inf")
        # for i in range(len(heights)) :
        #     a = find(i)
        #     res = max(a,res)
        # return res
        stack = []
        max_area = 0
        heights.append(0)
        for i in range(len(heights)) :
            while stack and heights[stack[-1]] > heights[i] :
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area,h*w)
            stack.append(i)
        return max_area
        

