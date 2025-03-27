

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def provera_resursa(naziv_kafe):
    if resources["water"] < MENU[naziv_kafe]["ingredients"]["water"]:
        print("Nije moguce napraviti kafu voda")
        return False
    elif resources["coffee"] < MENU[naziv_kafe]["ingredients"]["coffee"]:
        print("Nije moguce napraviti kafu kafa ")
        return False
    elif naziv_kafe == "latte" or naziv_kafe == "cappuccino":
        if resources["milk"] < MENU[naziv_kafe]["ingredients"]["milk"]:
            print("Nije moguce napraviti kafu mleko")
            return False
    print("Uspesno ste napravili kafu")
    return True



def umanji_resurse(naziv_kafe):
    resources["water"] -= MENU[naziv_kafe]["ingredients"]["water"]
    resources["milk"] -= MENU[naziv_kafe]["ingredients"]["milk"]
    resources["coffee"] -= MENU[naziv_kafe]["ingredients"]["coffee"]

def davanje_novca(naziv_kafe):
    quartes = int(input("Num of quarters: "))
    dimes = int(input("Num of dimes: "))
    nickles = int(input("Num of nickles: "))
    pennies = int(input("Num of pennies: "))
    money = quartes * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return money

radi = True

while radi:
    zelja = input("What would you like (espresso/latte/cappuccino): ")

    if zelja == "off":
        radi = False
    elif zelja == "report":
        print(resources)
    else:
        provera = provera_resursa(zelja)
        if provera:
            money = davanje_novca(zelja)
            if money < MENU[zelja]["cost"]:
                print("Niste ubacili dovoljno novca, vracam novac")
            else:
                umanji_resurse(zelja)
                kusur = round(money - int(MENU[zelja]["cost"]), 2)
                print(money)
                print(MENU[zelja]["cost"])
                print(f"Vracam kusur {kusur}")
        else:
            radi = False
            print("Masina se gasi nema dovoljno resursa")
