class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=len(s)
        switch=0
        ran=[]
        for l in s:
            
            if s.count(l)&1==True: 
                if switch==0:
                    switch=1
                elif switch==1 and l not in ran:
                    count-=1
                    print(l,count)
                ran.append(l)
        return count
        # d={}
        # count=0
        # for l in s:
        #     if l not in d:
        #         d={l:1} 
        #         print("added l")
        #     else: 
        #         d.update({l:+1})
        #         print("increased l")
        # print(d)
        # for el in d:
        #     ad=0
        #     if d[el]&1==False:
        #         count+=d[el]
        #         print("the count notched ",count)
        #     if d[el]&1==True and ad==0:
        #         count+=1
        #         ad=1
        #         print("the extra letter accounted")
        # return count-1