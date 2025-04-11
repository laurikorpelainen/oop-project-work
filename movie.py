class Movie:
    def __init__(self, id: str, title: str, length, director: str, age_rating: int):
        self.__id = id
        self.__title = title
        self.__length = length
        self.__director = director
        self.__age_rating = age_rating

    @property
    def id(self):
        return self.__id

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