class Seat:
    def __init__(self):
        self.__is_reserved = False

    def reserve_seat(self):
        self.__is_reserved = True