class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. Costruiamo il dizionario delle frequenze
        frequenze = {}
        for num in nums:
            frequenze[num] = frequenze.get(num, 0) + 1
            
        res = []
        
        # 2. Ripetiamo k volte la ricerca del massimo
        for _ in range(k):
            max_freq = -1
            max_num = None
            
            # Cerchiamo il numero con la frequenza più alta attuale
            for num, freq in frequenze.items():
                if freq > max_freq:
                    max_freq = freq
                    max_num = num
            
            # Aggiungiamo il numero trovato ai risultati
            res.append(max_num)
            
            # "Cancelliamo" questo numero mettendo la sua frequenza a -1
            # in modo che non venga più selezionato nel prossimo giro
            frequenze[max_num] = -1
            
        return res