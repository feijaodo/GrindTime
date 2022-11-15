class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.upper()
        cchar=[c for c in s if c.isalnum()]
        i=-1
        
        for c in cchar:
            if c != cchar[i]:
                return False
            i-=1
        return True
        