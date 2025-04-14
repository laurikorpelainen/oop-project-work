class User:
    __id_counter = 0

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
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
    
    def __str__(self):
        return f"User ID: {self.__id_counter}, Name: {self.__name}, Age: {self.__age}"