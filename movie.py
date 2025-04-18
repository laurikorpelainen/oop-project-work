from config import testing
class Movie:
    __id_counter = 0    # Counter to assign unique IDs

    def __init__(self, title: str, length: int, director: str, genre: str, age_rating: int):
        # Initialize a new Movie instance with given details
        if testing:
            assert isinstance(title, str) and len(title) > 0, "Title must be a non-empty string"
            assert isinstance(length, int) and length > 0, "Length must be a positive integer"
            assert isinstance(director, str) and len(director) > 0, "Director must be a non-empty string"
            assert isinstance(genre, str) and len(genre) > 0, "Genre must be a non-empty string"
            assert isinstance(age_rating, int) and age_rating >= 0, "Age rating must be a non-negative integer"

        self.__title = title
        self.__length = length
        self.__director = director
        self.__genre = genre
        self.__age_rating = age_rating
        Movie.__id_counter += 1 # Increment global movie ID counter

    @property
    def id(self):
        return self.__id_counter

    @property
    def length(self):
        return self.__length
    
    @property
    def title(self):
        return self.__title
    
    @property
    def director(self):
        return self.__director
    
    @property
    def age_rating(self):
        return self.__age_rating

    def __str__(self):
        # String representation of the Movie instance
        return f"Movie ID: {self.__id_counter}, Title: {self.__title}, Director: {self.__director}, Genre: {self.__genre}, Length: {self.__length}, Age-rating: {self.__age_rating}"
