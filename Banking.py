
# Banking project
class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        
        print(f"\nAccount {self.name} created.\nBalance = ${self.balance:.2f}")
        
    def getBalance(self):
        print(f"\nAccount {self.name}.\nBalance = ${self.balance:.2f}")
    
    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit Succesful.")
        self.getBalance()
        
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account {self.name} only has a balance of {self.balance:.2f}"
            )
            
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdrawal Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw interrupted: {error}!")
    
    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer...🚀 ")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete!✅\n\n**********")
        except BalanceException as error:
            print(f"Transfer interrupted! ❌ {error}!")
            
class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount  * 1.05)
        print("\nDeposit complete.")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw interrupted: {error}!")
            
if __name__ == "__main__":
    dave = BankAccount(1000, "Dave")
    sara = BankAccount(1000, "Sara")
    jim = InterestRewardsAcct(1000, "Jim")
    blaze = SavingsAcct(1000, "Blaze")

    dave.getBalance()
    dave.deposit(100000)
    dave.withdraw(10)
    dave.transfer(10000, sara)


    sara.deposit(500)
    sara.getBalance()


    jim.getBalance()
    jim.deposit(1000)
    jim.transfer(100, dave)

    blaze.getBalance()
    blaze.deposit(1000)
    blaze.transfer(1000, sara)