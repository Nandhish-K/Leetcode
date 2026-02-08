class Solution:
    def minimumDeletions(self, s: str) -> int:
        # d = {}
        # for i in range(len(s)) :
        #     count = 0
        #     for j in range(0,i) :
        #         if s[j] == 'b' :
        #             count += 1
        #     for k in range(i+1,len(s)) :
        #         if s[k] == 'a' :
        #             count += 1
        #     d[i] = count
        # minimum = float("inf")
        # for k in d :
        #     if d[k] < minimum :
        #         minimum = d[k]
        # return minimum
        # a_count_right = [0] * len(s)
        # for i in range(len(s) - 2,-1,-1) :
        #     a_count_right[i] = a_count_right[i+1]
        #     a_count_right[i] += 1 if s[i+1] == 'a' else 0
        # b_count_left = 0
        # res = len(s)
        # for i,c in enumerate(s) :
        #     res = min(res,b_count_left + a_count_right[i])
        #     if c == 'b' :
        #         b_count_left += 1
        # return res
        a_count_right = 0
        for c in s :
            a_count_right += 1 if c == 'a' else 0
        
        b_count_left = 0
        res = len(s)
        for i,c in enumerate(s) :
            if c == 'a' :
                a_count_right -= 1
            res = min(res,b_count_left + a_count_right)
            if c == 'b' :
                b_count_left += 1
        return res
