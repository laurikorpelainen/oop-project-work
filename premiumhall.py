from moviehall import MovieHall

class PremiumHall(MovieHall):
    def __init__(self, rows, columns, ticket_price=23.90, type='Premium'):
        super().__init__(type, rows, columns, ticket_price)