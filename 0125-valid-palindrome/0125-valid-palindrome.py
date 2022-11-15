class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[c for c in s.upper() if c.isalnum()]
        for i,c in enumerate(s):
            i+=1
            if c != s[-i]:
                return False
            
        return True
    
        