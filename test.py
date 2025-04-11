from standardhall import StandardHall
from premiumhall import PremiumHall
s = StandardHall(10, 10)
s.display_seats()
print(s.type)


p = PremiumHall(20, 20)
p.display_seats()
print(p.type)



"""ID counter not working correctly"""
print(s)
print(p)
"""Starts with ID 2 instead of 1"""