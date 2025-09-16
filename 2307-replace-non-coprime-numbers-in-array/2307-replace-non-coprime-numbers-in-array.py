class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums[:] :
            stack.append(num)
            while len(stack) >= 2 and gcd(stack[-1],stack[-2]) != 1 :
                last = stack.pop()
                second_last = stack.pop()
                new_number = lcm(last,second_last)
                stack.append(new_number)
        return stack
            
            
