class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind=len(numbers)-1
        i=0

        while True:
            if numbers[i]+numbers[ind]<target:
                i+=1
            elif numbers[i]+numbers[ind]>target:
                ind-=1
            else:
                arr=[i+1,ind+1]
                return arr
        
            