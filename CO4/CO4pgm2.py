class bankaccount:
    def __init__(self):
        self.acc_no=int(input("Enter the account number:"))
        self.name=input("Enter the name of the account holder:")
        self.acc_type=input("Enter the account type(S/C):")
        self.bal=0
    def deposit(self,amt):
        self.bal=self.bal+amt
        return(self.bal)
    def withdraw(self,amt):
        print("Balance:",self.bal)
        if self.bal<amt:
            print("Insufficient balance!")
        else:
            self.bal=self.bal-amt
        return(self.bal)
    def display(self):
        print("Account Number:",self.acc_no)
        print("Name:",self.name)
        print("Account type:",self.acc_type)
        print("Current Balance:",self.bal)
new_acc=bankaccount()
try:
    while True:
        print("Bank operations...\n1.Deposit\n2.Withdraw\n3.Display Account Details\n4.Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            amt=int(input("Enter the amount to be deposited:"))
            print("Current Balance:",new_acc.deposit(amt))
        elif ch==2:
           amt=int(input("Enter the amount to be withdrawn:"))
           print("Current Balance:",new_acc.withdraw(amt))
        elif ch==3:
            print("Account Details...")
            new_acc.display()
        else:
            print("Exit!")
            sys.exit(0)
except:
    print("Invalid data provided!")
finally:
    print("...Thank you for availing the banking facility...")
    