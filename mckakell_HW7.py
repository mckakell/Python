## HOMEWORK 7 ##

# PROBLEM 8.35 #

class Stack(object):

    def __init__(self):
        self.items=[] #empty list to beggin.
        
    def __str__(self):
        return str(self.items) # returns list

    def __len__(self):
        return len(self.items) #finds length of list
    
    def push(self, plate):
        self.items.append(plate) #adds plate 

    def pop(self):
        return self.items.pop() #removes plate

    def isEmpty(self):
        return len(self.items) == 0 #boolean if list is empty - True. If list is not empty - False is returned.



s = Stack()
s.push('plate 1') #adds plate to list
s.push('plate 2')
s.push('plate 3')
print(s)
s.pop() # removes plate from list
s.pop()
s.pop()
s.isEmpty() #True/False if list is empty



# PROBLEM 8.40 #
class BankAccount(object):

    def __init__(self, balance_amount=0): #automatically zero $ in account unless money is deposited
        self.balance_amount = balance_amount
        if balance_amount < 0:
            raise ValueError("Illegal Balance")#can't have less than zero $ in an account so Error message of Illegal Balance is shown
        
    def balance(self):
        return self.balance_amount #if someone wants to know their balance
    
    def deposit(self, deposit_amount):
        if deposit_amount < 0:
            raise ValueError("Negative Deposit")# if a negative deposit amount is attempted, this error message will show
        else:
            self.balance_amount += deposit_amount # if a valid deposit is made it will be added to the current balance
        
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance_amount: #You can't withdraw more money than is in the account, otherwise you will cause an overdraft
            raise ValueError("Overdraft")
        else:
            self.balance_amount -= withdraw_amount #if the withdraw is valid, it is subtracted from the current balance of the account.


try:
    x = BankAccount(-700) #testing a negative balance of -700. This will result in and Illegal Balance
except ValueError as e:
    print("ValueError", e)

try:
    x = BankAccount(0) # testing a withdraw of $70 when the current balance is $0. This will result in an overdraft.
    x.withdraw(70)
except ValueError as f:
    print("ValueError", f)

try:
    x = BankAccount(500) # testing a negative deposit. This will result in a "negative Deposit" error message
    x.deposit(-20)
except ValueError as g:
    print("ValueError",g)






