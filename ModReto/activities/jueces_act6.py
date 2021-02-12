"""
System used by judges to determine winner.

If two of the three judges are on, turn on led.
"""
def main():
    inputs = input("Ingrese el estado de los botones en bits de la forma X X X >>> ")
    checker = 0

    for i in inputs.split(' '):
        if i != "0" or i != "1":
            raise ValueError("Please use bits!")
        else: 
            checker += 1

    if checker >= 2:
        print("Foco prendido.")

    else: print("Foco no prendido.")

main()