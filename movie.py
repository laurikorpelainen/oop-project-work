class Movie:
    def __init__(self, id: str, title: str, length, director: str):
        self.__id = id
        self.__title = title
        self.__length = length
        self.__director = director

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