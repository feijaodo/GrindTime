class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=[l for l in set(s) if s.count(l)&1==True]
        if len(count)>=1:
            return len(s)-(len(count)-1)
        else:
            return len(s)