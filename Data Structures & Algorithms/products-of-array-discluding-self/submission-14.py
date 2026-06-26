class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr= [0]*len(nums)
        prod=1
        flag=False
        
        for k in range(len(nums)):  
            if(nums[k]!=0):
                prod=prod*nums[k]
            elif(flag):
                arr[:] = [0] * len(arr)
                return arr
            else:
                flag=True
                z=k

        for i in range(len(nums)):
            if(flag==True):
                if(i==z):
                    arr[z]=prod
                else:
                    arr[k]=0
            else:
                arr[i]=prod//nums[i]
            i+=i
        return arr