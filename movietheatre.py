from config import testing
from moviehall import MovieHall
class MovieTheatre:
    """
    Defines the MovieTheatre class representing a cinema location.
    Manages theater identity, halls, and scheduled screenings.
    """
    __id_counter = 0    # Counter to assign unique IDs

    def __init__(self, name: str, city: str, halls: list):
        # Initialize a theater with a name, city, and list of halls
        if testing:
            assert isinstance(name, str) and len(name) > 0, 'Name must be a non-empty string'
            assert isinstance(city, str) and len(city) > 0, 'City must be a non-empty string'
            assert isinstance(halls, list) and len(halls) > 0, 'Halls must be a non-empty list'
            assert all(isinstance(hall, MovieHall) for hall in halls), 'All halls must be MovieHall objects'

        self.__name = name
        self.__city = city
        self.__halls = halls
        self.__screenings = []
        MovieTheatre.__id_counter += 1 # Increment global movie ID counter

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
    def screenings(self):
        return self.__screenings
    
    def add_screening(self, screening: object):
        # Add a new screening to the theater
        if testing:
            assert isinstance(screening, object), 'Screening must be a Screening object'

        self.__screenings.append(screening)

    def add_hall(self, hall: MovieHall):
        # Add a new hall to the theater
        if testing:
            assert isinstance(hall, MovieHall), 'Hall must be a MovieHall object'

        self.__halls.append(hall)
    
    def __str__(self):
        # String representation of the MovieTheatre instance
        return f"Theater ID: {self.__id_counter}, Name: {self.__name}, City: {self.__city}"
        