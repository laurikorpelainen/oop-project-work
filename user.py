class User:
    def __init__(self, user_id: str, name: str, age: int):
        self.__user_id = user_id
        self.__name = name
        self.__age = age

    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    def is_adult(self):
        return self.__age > 18
    
    def __str__(self):
        return f"User_ID: {self.__user_id}, Name: {self.__name}, Age: {self.__age}"