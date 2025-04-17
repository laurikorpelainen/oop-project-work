class MovieTheatre:
    __id_counter = 0

    def __init__(self, name: str, city: str, halls: list):
        self.__name = name
        self.__city = city
        self.__halls = halls
        self.__screenings = []
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
    def halls(self):
        return self.__halls
    
    @property
    def screenigns(self):
        return self.__screenings
    
    def add_screening(self, screening: object):
        self.__screenings.append(screening)

    def add_theater(self, hall: object):
        self.__halls.append(hall)
    
    def __str__(self):
        return f"Theater ID: {self.__id_counter}, Name: {self.__name}, City: {self.__city}"
        