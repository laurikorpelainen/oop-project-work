class Screening:
    __id_counter = 0
    
    def __init__(self, movie, hall, time, date):
        self.__movie = movie
        self.__hall = hall
        self.__time = time
        self.__date = date
        Screening.__id_counter += 1
        self.__id = Screening.__id_counter
    
    @property
    def id(self):
        return self.__id
    
    @property
    def movie(self):
        return self.__movie
    
    @property
    def hall(self):
        return self.__hall
    
    @property
    def time(self):
        return self.__time
    
    @property
    def date(self):
        return self.__date
    
    def __str__(self):
        return f"Screening ID: {self.__id}, Movie: {self.__movie.title}, Date: {self.__date}, Time: {self.__time}"