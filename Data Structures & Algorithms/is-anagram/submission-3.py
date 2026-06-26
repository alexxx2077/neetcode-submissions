from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p1=Counter(s)
        p2=Counter(t)
        if(p1==p2):
            return True
        return False