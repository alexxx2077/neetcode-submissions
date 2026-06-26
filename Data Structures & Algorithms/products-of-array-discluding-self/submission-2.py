class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr= [0]*len(nums)
      

        for i in range(len(nums)):
            arr[i]=1
            for j in range(len(nums)):
                if(j!=i):
                    arr[i]=arr[i]*nums[j]

                j+=j

            i+=i
        return arr