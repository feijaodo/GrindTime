class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cList=image
        print(cList)
        
        fColor=image[sr][sc]
        print(fColor)
        if image[sr][sc]==color:
                return image
        #cList[sr][sc]=color
        #print(cList)
        
        #check each number
        #if the number is the same in adjoining number add to cList
        def check(sr,sc):
    
            if image[sr][sc]==fColor:
                image[sr][sc]=color
            
            if sr+1>-1 and sr+1<len(image) and image[sr+1][sc]==fColor:
                cList[sr+1][sc]=color
                check(sr+1,sc)

            if sr-1>-1 and sr-1<len(image) and image[sr-1][sc]==fColor:
                cList[sr-1][sc]=color
                check(sr-1,sc)

            if sc+1>-1 and sc+1<len(image[sr]) and image[sr][sc+1]==fColor:
                cList[sr][sc+1]=color
                check(sr,sc+1)

            if sc-1>-1 and sc-1<len(image[sr]) and image[sr][sc-1]==fColor:
                cList[sr][sc-1]=color
                check(sr,sc-1)

            return cList
        
        return check(sr,sc)
        
        