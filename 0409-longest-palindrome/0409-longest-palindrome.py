class Solution:
    def longestPalindrome(self, s: str) -> int:
        ineligible=[]
        for l in set(s):
            if s.count(l)&1==True:
                ineligible+=[l]
        if len(ineligible)==0:
            return len(s)
        else:
            return len(s)-len(ineligible)+1