from random import randint

class Budgets:
    def __init__(self, category: str,
        innitial_balance: float,
        running_balance: float) -> None:
        pass
        self.category = category
        self.innitial_balance = innitial_balance
        #private atribute
        self.running_balance = running_balance

    def get_running_balance(self) -> float:
        return self.running_balance
        
        
    def withdraw(self, amount:float):
        self.running_balance = self.running_balance - amount
        

    def deposit(self, amount:float):
        self.running_balance = self.running_balance + amount
        
class User:
    def __init__(self, name: str, total_budget: float) -> None:
        self.name = name
        self.total_budget = total_budget
        self.id = randint(0, 1000)
        self.budgets = dict
    
    

    def add_budget(self, category:str,
        innitial_balance: float):
        """
        create a budgets category
        """
        budgets = Budgets(category = category,
                    innitial_balance = innitial_balance)
        self.budgets.update({category: budgets})

    def transfer_balance(self, sender: str, receiver: str, amount: float):

        self.budgets[sender].withdraw(amount=amount)
        self.budgets[receiver].deposit(amount=amount)