from abc import ABC, abstractmethod

class Bank(ABC):
    
    def basicinfo(self):
        print("ça c'est une banque générique")

        return "Generic bank: 0"

    @abstractmethod
    def withdraw(self):
        pass

class Swiss(Bank):
   
    def __init__(self):
        self.bal = 1000
        
    def basicinfo(self):
        print("This is the Swiss Bank")
        return "Swiss Bank: " + str(self.bal)
    def withdraw(self, amount):
        if amount > self.bal:
            print("Insufficient funds")
            return self.bal
        else:
            self.bal -= amount
            print("Withdrawn amount: " + str(amount))
            print("New Balance: " + str(self.bal))
            return self.bal

def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()