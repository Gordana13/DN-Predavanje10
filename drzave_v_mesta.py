import random

def main():
    drzave_v_mesta = {
        "Slovenija": "Ljubljana",
        "Avstrija": "Dunaj",
        "Italija": "Rim",
    }

    drzava = random.randint(0, 2)
    izbrana_drzava = drzave_v_mesta.keys()[drzava]

    for drzava in drzave_v_mesta:
        uganjeno_mesto = raw_input("Katero je glavno mesto drzave %s: " %izbrana_drzava)

        preveri(drzava, uganjeno_mesto, drzave_v_mesta)


def preveri(drzava, uganjeno_mesto, drzave_v_mesta):
    dejansko_mesto = drzave_v_mesta[drzava]
    if uganjeno_mesto == dejansko_mesto:
        print("Pravilno")
    else:
        print("Napacno")


if __name__ == '__main__':
    main()