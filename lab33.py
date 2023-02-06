from random import randint
from random import randrange

print("Сколько лет Адилету?", randint(0, 25))
print("Сколько лет Адилету?", randint(0, 25))

print("Сколько лет маме Адилета?", randrange(38, 40, 56))

family = ['Adilet', 'Gulnaz', 'Aizhan']
print(list(enumerate(family, start=1)))