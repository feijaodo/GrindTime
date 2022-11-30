class Solution:
    def longestPalindrome(self, s: str) -> int:
        switch=0
        ineligible=0
        for l in set(s):
            print(l)
            if s.count(l)&1==True:
                if switch==1:
                    ineligible+=1
                else:
                    switch=1
        return len(s)-ineligible