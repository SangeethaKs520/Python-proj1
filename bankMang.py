# User Details

# Holds details about an user
class User():
    def __init__(self, name, age, gender,type):
        self.name = name
        self.age = age
        self.gender = gender
        self.type = type

# Function to show user details
    def Show_User_Details(self):
        print("Personal details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender:", self.gender)
        print("Type:",self.type)
        f= open("userDetail.txt","w")
        f.write("")
        f.write(self.name)
        f.write(str(self.age))
        f.write(self.gender)
        f.close()


# Bank details. Child class

class Bank(User):
    def __init__(self,name, age, gender,type):
     super(). __init__(name, age, gender,type)
   
    def AccountType(self,type):
        self.type = type
        if self.type == "S" or self.type == "s":
          f = open("bankDetails.txt", "r")
          self.minBalance = f.read()
          f.close()
          if int(self.minBalance) < 500:
            print("You cannot withdraw because your balance is low")
            print("Savings account minimum Balance should be 500 or above 500")
            print("Please deposit 500 rupees to account to contiue")
            self.minBalance = int(input("Enter the amount that you want to deposit")) + int(self.minBalance)
            self.SavingsAccount(self.type)
          else:
            self.SavingsAccount(self.type)
              
        elif self.type == "C" or self.type == "c":
          f = open("bankDetails.txt", "r")
          self.minBalance = f.read()
          f.close()
          if int(self.minBalance) < 2000:
            print("You cannot withdraw because your balance is low")
            print("Current account minimum Balance should be 2000 or above 2000")
            self.minBalance = int(input("Enter the amount that you want to deposit")) + int(self.minBalance)
            self.CurrentAccount(self.type)
          else:
            self.CurrentAccount(self.type)
         
          
    def SavingsAccount(self,type):
        self.type = type
        DW=input("Do you want to deposit or withdraw amount[d/w]: ")
        if DW=="d" or DW == "D":
            self.Deposit()
        elif DW=="w" or DW == "W":
            print("working")
            self.Withdraw()
            
    def CurrentAccount(self,type):
        DW=input("Do you want to deposit or withdraw amount[d/w]: ")
        if DW=="d" or DW == "D":
            self.Deposit()
        elif DW=="w" or DW == "W":
            print("working")
            self.Withdraw()
            
            
            
            
    def Deposit(self):
        self.deposit=0
        self.amount =int(self.minBalance)
        self.deposit=int(input("Enter the amount u want to deposit: "))
        self.deposit = self.amount + self.deposit
        f = open("bankDetails.txt", "w")
        f.write(str(self.deposit))
        f.close()
        f = open("bankDetails.txt", "r")
        print("Now your balance is updated to Rupees",int(f.read()))
        f.close()
        
       

    def Withdraw(self):
      self.withdraw_amount =int(input("Enter the amount you want to withdraw: "))
      f = open("bankDetails.txt", "r")
      self.balance = f.read()
      if(self.type == "s"):
        if(self.withdraw_amount > int(self.balance)):
         f = open("bankDetails.txt", "r")
        # f.write(str(self.balance))
         print("Can't withdraw, because available balance is less than withdrawing amount and balance amount is Rupees",f.read(int(self.balance)))
         f.close()  
        else:
            self.balance = int(self.balance)-self.withdraw_amount
            f = open("bankDetails.txt", "w")
            f.write(str(self.balance))
            f.close()
            
            f = open("bankDetails.txt", "r")
            print("Available balance is", f.read(int(self.balance)))
            
      elif(self.type == "c"):
        if(self.withdraw_amount > int(self.balance)):
         f = open("bankDetails.txt", "r")
         print("Amount overdrawn")
         f.close()



obj1 = Bank("raju",21,"Male","c")
obj1.Show_User_Details()
obj1.AccountType("c")



