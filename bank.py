class BankAccountgit:
    def __init__(self,balance=0):
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"ฝากเงินจำนวน {amount} สำเร็จ")
        else:
            print("ยอดเงินไม่เพียงพอ")
    
    def withdraw(self,amount):
        if amount > 0 and :
            print("ยอดเงินไม่เพียงพอ")
        elif