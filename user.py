class User:
    __id_counter = 0

    def __init__(self, name: str, age: int, balance: float):
        self.__name = name
        self.__age = age
        self.__balance = balance
        User.__id_counter += 1

    @property
    def user_id(self):
        return self.__id_counter
    
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @property
    def balance(self):
        return self.__balance
    
    def add_funds(self, amount: float):
        self.__balance += amount

    def decrease_funds(self, amount: float):
        self.__balance -= amount
    
    def __str__(self):
        return f"User ID: {self.__id_counter}, Name: {self.__name}, Age: {self.__age}"