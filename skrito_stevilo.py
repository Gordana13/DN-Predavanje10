# -*- coding: utf-8 -*-
import random

def main():
    skrito_stevilo = random.randint(1, 15)

    while True:
        ugani = int(raw_input("Ugani skrito število med 1 in 15: "))

        if ugani == skrito_stevilo:
            print("Pravilno")
            break
        elif ugani > skrito_stevilo:
            print("Tvoje število je previsoko.")
        elif ugani < skrito_stevilo:
            print("Tvoje število je prenizko.")

if __name__ == '__main__':
    main()