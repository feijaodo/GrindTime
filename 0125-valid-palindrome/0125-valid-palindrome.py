class Solution:
    def isPalindrome(self, s: str) -> bool:
        aug=0
        for i,c in enumerate(s,1):
            index=-i+aug
            
            if c.isalnum()==False:
                aug+=1
                continue
            while s[index].isalnum()==False:
                    index-=1
                    aug-=1
                    print(aug,index,c,s[index])
                    pass
            #if index*-1>len(s)/2:
             #   break
            if c.upper() != s[index].upper():
                print('comparing',c,s[index])
                return False
                
        return True
    
        