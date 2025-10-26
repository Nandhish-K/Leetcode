class ATM:
    

    def __init__(self):
        self.notes = [0]*5
        self.values = [20,50,100,200,500]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)) :
            self.notes[i] += banknotesCount[i]


        

    def withdraw(self, amount: int) -> List[int]:
        res = [0]*5
        remaining = amount
        for i in range(4,-1,-1) :
            available = self.notes[i]
            use = min(remaining//self.values[i],available)
            res[i] = (use)
            remaining -= use * self.values[i]
        if remaining != 0 :
            return [-1]
        for j in range(5) :
            self.notes[j] -= res[j]
        return res

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)