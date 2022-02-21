class Atm():
    def __init__(self,cardno,company,amount) :
        self.cardno=cardno
        self.company=company
        self.amount=amount
    
    def User(self):
        print("Your card number is {self.cardno}\n Its {self.company} card\n Amount to withdraw {self.amount}")
    
Yash=Atm("5555 5555 5555 5555","visa","10,000")
Yash.User()
        