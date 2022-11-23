class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=3,2
        if n>3:
            for num in range(n-3):
                one,two=one+two,one
        else:
            one=n
        return one
            
        