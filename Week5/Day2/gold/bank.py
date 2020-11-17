from getpass import getpass
# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#     # def deposit(self, amount):
#     #     self.balance += amount
#         # def withdraw(self, amount):
#         #     self.balance -= amount
    
    
class Owner:
    def __init__(self, owner, balance, credit_number, password):
        self.owner = owner
        self.balance = balance
        self.credit_number = credit_number
        self.password = password
    def check_owner_info(self):
        identify = False
        while identify == False:
            user_number = int(input("Input credit card number: "))
            if user_number != self.credit_number:
                print("This credit card number is invalid.")
            else:
                identify = True
        attempt_counter = 0
        while attempt_counter<2:
            attempt = getpass()
            if attempt != self.password:
                attempt_counter +=1
                print("Incorrect password entered.")
            else:
                print("Login successful")
                print(f"Welcome. Current Balance: {self.balance}")
                choice = input("Would you like to deposit or withdraw? (d/w): ")
                if choice.lower() == "d":
                    depositing = True
                    while depositing:
            
                        bill = int(input("Enter your first bill into machine. Enter 0 to stop: "))
                        if bill in [20,50,100]:
                            self.balance += bill
                            print(f"{bill} added. Current balance: {self.balance}")
                            
                        elif bill == 0:
                            print(f"New balance : {self.balance}")
                            depositing = False
                            
                        else:
                            print("Invalid bill entered")

                elif choice.lower() == "w":
                    withdrawal_amount = int(input("How much would you like to withdraw? "))
                    if withdrawal_amount>self.balance:
                        print(f"You do not have sufficient funds in the account. Find a job.")
                    elif withdrawal_amount < 20 or withdrawal_amount%10 !=0:
                        print("Invalid amount entered. Please enter a valid value.")
                    else:
                        withdrawing = True
                        cash_out = []
                        while withdrawing:
                            while withdrawal_amount - sum(cash_out) > 20:
                                cash_out.append(50)
                            if withdrawal_amount == sum(cash_out):
                                print("withdrawal complete")
                            else:
                                cash_out.append(20)
                            withdrawing = False
                    
                        print(cash_out)
                        self.balance -= withdrawal_amount
                        print(f"{withdrawal_amount} withdrawn. New balance: {self.balance}")
    
        else:
            print("Too many attempts. Account deleted")
            del self.credit_number
            del self.password
   

o1 = Owner("mike", 1000, 123, "test")
o1.check_owner_info()