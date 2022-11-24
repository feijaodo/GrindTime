class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=5,3
        if n>3:
            for num in range(n-4):
                one,two=one+two,one
        else:
            return n
        return one
            
        