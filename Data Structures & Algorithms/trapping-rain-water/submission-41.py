class Solution:
    def trap(self, height: List[int]) -> int:
        


        if not height or len(height) < 3:
            return 0



        usatosx=False
        

        mstacksx = []
        mstackdx = []
        i=0
        j=len(height)-1
        

       
        #trovo massimo
        mas = max(height)
        masid = height.index(mas)


        while(i<=masid or j>=masid):
            if(i<=masid):
                if (not mstacksx or height[i]>=height[mstacksx[-1]]) and height[i]>0:
                    mstacksx.append(i)
                    usatosx=True
            if(j>=masid):
                if (not mstackdx or height[j]>=height[mstackdx[-1]]) and height[j]>0: #serve >0???
                    mstackdx.append(j) 
                    
    
            i+=1
            j-=1

        print(mstacksx, mstackdx)


        if(usatosx==False):
            return 0

        # acqua a sx

        k = mstacksx[0]
        i = 0
        j = 1
        acquazzasx =0
        
        while j<len(mstacksx):
            
            sx=height[mstacksx[i]]
            dx=height[mstacksx[j]]
           
    
            while k<mstacksx[j]:
                acquazzasx+=sx-height[k]
                k+=1


            i+=1
            j+=1

        z = mstackdx[0]
        i = 0
        j = 1
        acquazzadx =0
        
        while j<len(mstackdx):
            sx=height[mstackdx[i]]
            dx=height[mstackdx[j]]
           
    
            while z>mstackdx[j]:
                acquazzadx+=sx-height[z]
                z-=1


            i+=1
            j+=1

        

        return acquazzadx + acquazzasx 



                






