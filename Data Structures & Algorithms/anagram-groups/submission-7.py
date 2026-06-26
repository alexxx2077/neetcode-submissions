class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r=defaultdict(list)
        
        for i in strs:
            hsh=[0]*26
            for j in i:
                hsh[ord(j)-ord('a')]+=1
            r[tuple(hsh)].append(i)
        return list(r.values())