class Seat:
    def __init__(self, row, collumn):
        self.__row = row
        self.__collumn = collumn
        self.__is_reserved = False

    @property
    def row(self):
        return self.__row

    @property
    def collumn(self):
        return self.__collumn

    def reserve_seat(self):
        self.__is_reserved = True

    def __str__(self):
        if self.__is_reserved == True:
            return "1"
        return "0"