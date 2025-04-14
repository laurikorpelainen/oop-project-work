from moviehall import MovieHall

class StandardHall(MovieHall):
    def __init__(self, rows, columns, type='Standard'):
        super().__init__(type, rows, columns)