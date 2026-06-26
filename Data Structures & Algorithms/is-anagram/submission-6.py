from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p1= {}
        p2= {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            p1[s[i]]=1+p1.get(s[i],0)
            p2[t[i]]=1+p2.get(t[i],0)
        return p1==p2