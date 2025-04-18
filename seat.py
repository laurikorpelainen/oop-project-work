from config import testing
class Seat:
    def __init__(self, row: int, column: int):
        if testing:
            assert isinstance(row, int) and row >= 0, 'Row must be a postive integer'
            assert isinstance(column, int) and column >= 0, 'Row must be a positive integer'

        self.__row = row
        self.__column = column
        self.__is_reserved = False

    @property
    def row(self):
        return self.__row

    @property
    def column(self):
        return self.__column
    
    @property
    def is_reserved(self):
        return self.__is_reserved

    def reserve_seat(self):
        self.__is_reserved = True

    def __str__(self):
        if self.__is_reserved == True:
            return "1"
        return "0"