from cinemachain import Cinemachain
from movietheatre import MovieTheatre
from moviehall import MovieHall
from movie import Movie
from seat import Seat
from user import User
import tkinter
from tkinter import ttk, messagebox

class BookingApplication:
    def __init__(self, users: list):
        self.__users = []
        self.__root = tkinter.Tk()
        self.__root.title("Movie Booking App")
        self.__root.geometry("800x600")
        self.__setup_ui()

    def __setup_ui(self):
        #Frames
        self.__login_frame = ttk.Frame(self.__root, padding="10")

        #Components
        

    def register_user(self, user: User):
        self.__users.append(user)

    def run(self):
        self.__root.mainloop()

if __name__ == "__main__":
    a = BookingApplication(["a"])
    a.run()