class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # salvo lettere viste in hashmap con i loro indici, quando trovo un duplicato sposto il primo carattere da cui controllare la stringa al successivo della prima lettera individuata fra le due identiche, togliendo dall'hashmap le lettere posizionate fra la prima lettera della stringa in controllo precedentemente e quella da cui parte il nuovo controllo, fermo il controllo quando mi mancano poche lettere, minori della lunghezza della stringa più lunga trovata

        # dizionario inizializzato:

        ascii_map = {}
        out=0
        i=0
        iniz=0
        outmax=0
        
        while (i < len(s)):
            while i < len(s)  and (s[i] not in ascii_map):
                ascii_map[s[i]] = i
                i+=1
                
            
            if i-iniz>outmax:
                outmax=i-iniz

            if(i==len(s)):
                break

            temp=iniz
            iniz=ascii_map[s[i]]+1
                # liberiamo l'hashmap fra temp e iniz
 
            for j in range(temp, iniz):
                ascii_map.pop(s[j])
                
            ascii_map[s[i]] = i
            
            i += 1
        return outmax

                        


        