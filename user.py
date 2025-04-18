from config import testing
class User:
    __id_counter = 0    # Counter to assign unique IDs

    def __init__(self, name: str, age: int, balance: float):
        if testing:
            assert isinstance(name, str) and len(name) > 0, "Name must be a non-empty string"
            assert isinstance(age, int) and age >= 0, "Age must be a non-negative integer"
            assert isinstance(balance, float) and balance >= 0, "Balance must be a non-negative float"

        self.__name = name
        self.__age = age
        self.__balance = balance
        User.__id_counter += 1  # Increment global movie ID counter

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
        """Adds amount of funds to users balance"""
        if testing:
            assert isinstance(amount, float) and amount > 0, "Amount must be a positive float"

        self.__balance += amount
        return f"{amount}€ added \nCurrent balance now is {self.__balance}€"

    def decrease_funds(self, amount: float):
        """Decreases amount of funds from users balance"""
        if testing:
            assert isinstance(amount, float) and amount > 0, "Amount must be a positive float"
            assert self.__balance >= amount, "Insufficient funds"

        self.__balance -= amount
    
    def __str__(self):
        """String representation of user instance"""
        return f"User ID: {self.__id_counter}, Name: {self.__name}, Age: {self.__age}"