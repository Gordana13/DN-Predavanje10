import random

def loto_generator():
    print("Welcome to the Lottery numbers generator.")
    seznam = []

    number = int(raw_input("Please enter how many random numbers would you like to have: "))
    print("User: %s" %number)

    seznam = random.sample(xrange(1, 30+1), number)
    return seznam

print loto_generator()
print("END")