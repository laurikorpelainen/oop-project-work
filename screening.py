from config import testing
from moviehall import MovieHall
from movietheatre import MovieTheatre
from movie import Movie
class Screening:
    """
    Defines the Screening class representing a scheduled movie showing.
    Includes information about the movie, hall, theater, time, and date.
    """
    __id_counter = 0    # Counter to assign unique IDs
    
    def __init__(self, movie: Movie, hall: MovieHall, time: str, date: object, theater: MovieTheatre):
        if testing:
            assert isinstance(movie, Movie), "Movie must be a Movie object"
            assert isinstance(hall, MovieHall), "Hall must be a MovieHall object"
            assert isinstance(time, str) and len(time) > 0, "Date must be a non-empty string"
            assert isinstance(date, object), "Time must be a datetime object"
            assert isinstance(theater, MovieTheatre), "Theater must be a MovieTheatre object"

        self.__movie = movie
        self.__hall = hall
        self.__time = time
        self.__date = date
        self.__theater = theater
        Screening.__id_counter += 1
        self.__id = Screening.__id_counter  # Increment global movie ID counter
    
    @property
    def theater(self):
        return self.__theater

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
        # String representation of the Screening instance
        return f"Screening ID: {self.__id}, Movie: {self.__movie.title}, Date: {self.__date}, Time: {self.__time}"