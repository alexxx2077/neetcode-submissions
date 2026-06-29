class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        lis: list[list[int]] = []
        for i in range(len(nums)): #primo dei 3 numeri richiesti
        #per trovare gli altri due uso due puntatori
            if i>0 and nums[i]==nums[i-1]:
                continue


            j=i+1
            k=len(nums)-1
            while(j<k):
                if nums[j]+nums[k]+nums[i]<0:
                    j+=1
                elif nums[j]+nums[k]+nums[i]>0:
                    k-=1
                else:
                    lis.append([nums[i],nums[j],nums[k]])
                    k-=1
                    j+=1 
                    while(nums[k]==nums[k+1] and j<k):
                        k-=1
                    
                    while(nums[j]==nums[j-1] and j<k):
                        j+=1
        return lis
