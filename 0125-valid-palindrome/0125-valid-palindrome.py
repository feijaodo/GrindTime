class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[c for c in s.upper() if c.isalnum()]
        for i,c in enumerate(s,1):
            print(i)
            if c != s[-i]:
                return False
            elif i>len(s)/2:
                break

        return True
    
        