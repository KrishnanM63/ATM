class atm:
    def __init__(self,balance,pin):
        self.balance=balance
        self.pin=pin
    def pincheck(self):
        if(self.pin==1234):
            print("your login sucessfully")
            return True
        else:
            print("your pin is wrong")
            return False   

    def view_balance(self):
        print(f"your current balance is{self.balance}")

    def add_balance(self,amount):
        self.balance=self.balance+amount 
        print(f"Deposit amount is ₹{amount}")
        self.view_balance()

    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdraw amount ₹{amount}")
            withdraw=self.balance- amount 
            self.view_balance()

        else:
            print("Insufficient balance")





pin=int(input("enter your pin:"))             
krish=atm(200,pin)
if krish.pincheck():
    while True:

        print("===ATM====")
        print("1.check balance")
        print("2.Deposit balance")
        print("3.Withdraw balance")
        print("4.Exit")

        choice=int(input("enter your choice:"))
        if choice==1:
            krish.view_balance()
        elif choice==2:
            amount=int(input("Enter the deposit amount"))
            krish.add_balance(200)
        elif choice==3:
            amount=int(input("Enter the withdraw amout"))
            krish.withdraw(amount)
        elif choice==4:
            print("Thank you for using ATM")
        else:
            print("invalid choice! try again")        
      




    
