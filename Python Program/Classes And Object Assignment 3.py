# Create classes that capture bank customers and bank accounts. A customer has a first and last
# name. An account has a customer and a balance. Make objects for two accounts held by the
# same customer.
class BankCustomers:
    def __init__(self,firstname,lastname):
        self.fn=firstname
        self.ln=lastname
    def display(self):
        self.fullname=self.fn+" "+self.ln
        print("Customer Full Name:", self.fullname)
        print("Account Detail".center(50, "*"))

class BankAccounts:
    i=0
    def __init__(self,balance):
        BankAccounts.i+=1
        self.b=balance
    def show(self):
        print("Account",BankAccounts.i,"Balance:",self.b)

c1=BankCustomers("Rucha","Rajurkar")
customer=c1.display()
account1=BankAccounts(5000)
account1.show()
account2=BankAccounts(7000)
account2.show()