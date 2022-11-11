class Solution:
    def isValid(self, s: str) -> bool:
        log=[]
        if len(s)<2:
            return False
        for sym in s:
            if sym==("(") or sym==("{")or sym==("["):
                log.append(sym)
            elif sym==(")") :
                try:
                    check=log.pop()
                except IndexError:
                    return False
                if check!="(":
                    return False
            elif sym==("]") :
                try:
                    check=log.pop()
                except IndexError:
                    return False
                if check!="[":
                    return False
            elif sym==("}") :
                try:
                    check=log.pop()
                except IndexError:
                    return False
                if check!="{":
                        return False
        if len(log)>0:
            return False
        return True
    
    
    
    
    
    """" openP=0
        openB=0
        openC=0
        lSymbol=""
        for symbol in s:
            print(lSymbol)
            if (openP or openB or openC) < 0:
                return False
        
            if symbol=="(":
                openP+=1
            elif symbol==")":
                openP-=1
                if lSymbol=="{" or lSymbol=="[":
                    return False
                
            elif symbol=="[":
                openB+=1
            elif symbol=="]":
                openB-=1
                if lSymbol=="{" or lSymbol=="(":
                    return False
                
            elif symbol=="{":
                openC+=1
            elif symbol=="}":
                openC-=1
                if lSymbol=="(" or lSymbol=="[":
                    return False
                
            lSymbol=symbol
        if openP==0 and openB==0 and openC==0:
            return True"""