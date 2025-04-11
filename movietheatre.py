class MovieTheatre:
    __id_counter = 1

    def __init__(self, name: str, city: str, hall_amount: int):
        self.__name = name
        self.__city = city
        self.__hall_amount = hall_amount
        MovieTheatre.__id_counter += 1

    @property
    def theater_id(self):
        return self.__id_counter
    
    @property
    def name(self):
        return self.__name
    
    @property
    def city(self):
        return self.__city
    
    @property
    def hall_amount(self):
        return self.__hall_amount
    
    def __str__(self):
        return f"Theater ID: {self.__id_counter}, Name: {self.__name}, City: {self.__city}, Hall amount: {self.__hall_amount}"
        