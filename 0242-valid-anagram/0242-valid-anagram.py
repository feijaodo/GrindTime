class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        
        for l in s:
            t=t.replace(l,"",1)
            
        if len(t)!=0:
            return False
        return True
    
    """if s.count(l)!=t.count(l):
                return False"""