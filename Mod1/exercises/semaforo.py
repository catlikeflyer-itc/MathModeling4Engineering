
def main():
    camas = input('Camas elevadas (si/no): ')
    vents = input('Ventiladores altos: (si/no): ')
    posi_alt = input('Positividad alta (si/no): ')
    verdades = 0

    l = [camas, vents, posi_alt]
    for i in l:
        if i == "si":
            verdades += 1

    if verdades >= 2:
        print('Semaforo rojo')
    elif verdades == 1:
        print('Semaforo amarillo')
    else:
        print('Semaforo verde')
    
if __name__ == "__main__":
    main()





