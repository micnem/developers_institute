class Currency:
    def __init__(self, currency_name, amount):
        self.currency_name = currency_name
        self.amount = amount
    def __str__(self):
        return f"{self.amount} {self.currency_name}"
    def __int__(self):
        return self.amount
    def __add__(self, other):
        if isinstance(other, int): 
            return self.amount + other
        else:
            if self.currency_name == other.currency_name:
                return self.amount + other.amount
            else:
                print(f"TypeError: Cannot add between Currency type {self.currency_name} and {other.currency_name}")
    def __repr__(self):
        return str(self.amount) + " " + self.currency_name + "s"
    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
            return self
            
        else:
            if self.currency_name == other.currency_name:
                self.amount += other.amount
                return self
            else:
                print(f"TypeError: Cannot add between Currency type {self.currency_name} and {other.currency_name}")

     
            


            