import random
import sys

def main():
    while True:
        if random.randint(0,10) > 5:
            print("Exiting...")
            sys.exit()
        else:
            continue

main()   
        
        