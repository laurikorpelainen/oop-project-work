from cinemachain import Cinemachain
from movietheatre import MovieTheatre
from moviehall import MovieHall
from movie import Movie
from seat import Seat
from user import User

class BookingApplication:
    def __init__(self, users: list):
        self.__users = []

    def register_user(self, user: User):
        self.__users.append(user)
