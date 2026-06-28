class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            le=len(numbers)-1
            s=i+1
            dif=target-numbers[i]
            while s<=le:
                ind=s+(le-s)//2
                if numbers[ind]==dif:
                    return [i+1,ind+1]
                elif numbers[ind]<dif:
                    s=ind+1
                else:
                    le=ind-1
        return []
        