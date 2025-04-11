from moviehall import MovieHall
class PremiumHall(MovieHall):
    def __init__(self, rows, collumns, type='Premium'):
        super().__init__(type, rows, collumns)