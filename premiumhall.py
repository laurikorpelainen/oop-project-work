from moviehall import MovieHall

class PremiumHall(MovieHall):
    def __init__(self, rows, columns, type='Premium'):
        super().__init__(type, rows, columns)