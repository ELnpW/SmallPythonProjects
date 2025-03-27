import random
import art
from game_data import data

print(art.logo)

score = 0

corect = True

personA = random.choice(data)
personB = random.choice(data)

while corect:
    print("\n")
    print("\n")
    print(f"Your score is: {score}")
    print(personA["name"])
    print(personA["description"])
    print(personA["follower_count"])

    print(art.vs)

    print(personB["name"])
    print(personB["description"])
    print(personB["follower_count"])

    izbor = input("Izaberi a ili b: ")

    if izbor == 'a' and personA["follower_count"] > personB["follower_count"]:
        score += 1
        personB = random.choice(data)
    elif izbor == 'b' and personA["follower_count"] < personB["follower_count"]:
        tmpp = personB
        personA = personB
        personB = random.choice(data)
        score += 1
    elif izbor == 'b' and personA["follower_count"] > personB["follower_count"]:
        corect = False
    elif izbor == 'a' and personA["follower_count"] < personB["follower_count"]:
        corect = False

