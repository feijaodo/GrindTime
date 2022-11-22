# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        a=0
        b=(n)
        t=0
        while a<b:
            t=(b+a)//2
            if isBadVersion(t) and isBadVersion(t-1)==False:
                return t
            elif isBadVersion(t)==False and isBadVersion(t+1)==True:
                return t+1
            elif isBadVersion(t):
                b=t
            else:
                a=t
        return 1