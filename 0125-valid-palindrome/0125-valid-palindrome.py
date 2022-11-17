class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[c for c in s.upper() if c.isalnum()]
       # print(s[0:int(len(s)/2)+1:1],s[-1:-(int(len(s)/2)+2):-1])
        if s[0:int(len(s)/2)+1:1]==s[-1:-(int(len(s)/2)+2):-1]:
            return True
        return False