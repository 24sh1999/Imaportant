class cus:
    counter = 100
    print("I am ready to go")
    def __init__(self):
        self.cus_id = cus.counter
        cus.counter += 1
        self.discount = 5
    def calculate_total_amt(self,amt):
        return amt*(100-self.discount) / 100

class pri(cus):
    def __init__(self):
        super().__init__()
        self.pri_point = 100
    def calculate_total_amt(self,amt):
    	amt = super().calculate_total_amt(amt) #Line = 1
    	return amt - (self.pri_point + amt)//10 # Line = 2
pri_customer  = pri()
print('customer id:', pri.counter   )#Line = 3
print('Amount',pri_customer.calculate_total_amt(1000))

