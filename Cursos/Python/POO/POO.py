class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hola mi nombre es {self.name} y tengo {self.age}')

person1 = Person('Sebastian', 23)
person2 = Person('Pepito', 73)

person1.greet()
person2.greet()

print('___________________________________________')

class BanckAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f'Se ha depositado {amount}. Saldo total {self.balance}')
        else:
            print('Accion invalida, no se puede depositar a una cuenta inactiva')
        
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f'Se a retirado {amount}. Saldo actual {self.balance}')

    def desactivate_account(self):
        self.is_active = False
        print('Se ha desctivado la cuenta')

    def activate_account(self):
        self.is_active = True
        print('Se ha activado la cuenta')

account1 = BanckAccount('Ana', 500)
account2 = BanckAccount('Francisco', 4000)

account1.deposit(200)
account2.deposit(200)

account1.desactivate_account()
account1.deposit(100)

account1.activate_account()
account1.deposit(100)