from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        r=defaultdict(int)
        mx=0
        for i in nums:
            if (not r[i]):
                r[i] = r[i+1] + r[i-1] + 1
                
                #
                r[i - r[i - 1]] = r[i]
                r[i + r[i + 1]] = r[i]
                #cambio il rank degli elementi all'inizio e alla fine della sequenza
                if(mx < r[i]):
                     mx=r[i]

        return mx

        