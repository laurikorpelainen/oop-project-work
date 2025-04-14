class Movie:
    __id_counter = 0

    def __init__(self, title: str, length, director: str, genre: str, age_rating: int):
        self.__title = title
        self.__length = length
        self.__director = director
        self.__genre = genre
        self.__age_rating = age_rating
        Movie.__id_counter += 1

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
        return f"Movie ID: {self.__id_counter}, Title: {self.__title}, Director: {self.__director}, Genre: {self.__genre}, Length: {self.__length}"
