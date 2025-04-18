from config import testing
from moviehall import MovieHall
class MovieTheatre:
    __id_counter = 0

    def __init__(self, name: str, city: str, halls: list):

        if testing:
            assert isinstance(name, str) and len(name) > 0, 'Name must be a non-empty string'
            assert isinstance(city, str) and len(city) > 0, 'City must be a non-empty string'
            assert isinstance(halls, list) and len(halls) > 0, 'Halls must be a non-empty list'
            assert all(isinstance(hall, MovieHall) for hall in halls), 'All halls must be MovieHall objects'

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
        if testing:
            assert isinstance(screening, object), 'Screening must be a Screening object'

        self.__screenings.append(screening)

    def add_theater(self, hall: MovieHall):
        if testing:
            assert isinstance(hall, MovieHall), 'Hall must be a MovieHall object'

        self.__halls.append(hall)
    
    def __str__(self):
        return f"Theater ID: {self.__id_counter}, Name: {self.__name}, City: {self.__city}"
        