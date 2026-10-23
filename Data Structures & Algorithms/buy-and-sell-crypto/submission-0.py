class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ogni elemento indica valore per giornata, scelgo un giorno per comprare uno per vendere, return massimo profitto, posso non fare transazioni per avere 0

        #posso scorrere l'array tenendo a mente il minimo e calcolando quanto guadagnerei ad ogni passo

        pro=0

        mini = prices[0]
        for i in range(1,len(prices)):
            if (prices[i]<mini):
                mini=prices[i]
            val=prices[i]-mini
            if val>pro:
                pro=val

        return pro