class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        
        for l in s:
            if s.count(l)!=t.count(l):
                return False
        
        return True