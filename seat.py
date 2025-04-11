class Seat:
    def __init__(self):
        self.__is_reserved = False

    def reserve_seat(self):
        self.__is_reserved = True

    def __str__(self):
        if self.__is_reserved == True:
            return "1"
        return "0"