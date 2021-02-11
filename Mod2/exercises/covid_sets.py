"""
Take a set of pacient names and assign is they present one of 
two symptoms of COVID19 (coughing, and fever). 
"""

def get_names():
    pacient_num = int(input("How many people are there?: "))
    pacients = []
    coughs = []
    fevers = []
    
    for i in range(0, pacient_num):
        name = input("Name: ")
        cough = input("Coughing (y/n): ")
        fever = input("Fever (y/n): ")
        
        pacients.append(name)

        if cough == "y":
            coughs.append(name)
        
        if fever == "y":
            fevers.append(name)

    return pacients, coughs, fevers

def print_names(lis: list, concept:str):
    print(concept+'\n')
    for i in lis:
        print(i+"\n")

    print(f'Cardinality: {len(lis)}\n')

def main():
    pacients, cough, fever = get_names()
    print_names(pacients, "---All Pacients---")
    print_names(cough, "---Pacients with coughing---")
    print_names(fever, "---Pacients with fever---")

    pacients = set(pacients)
    cough = set(cough)
    fever = set(fever)

    cough_fever = cough.intersection(fever)
    no_symptoms = pacients-fever-cough

    print_names(cough_fever, "---Pacients with both symptoms---")
    print_names(no_symptoms, "--No symptoms---")

main()

        
        

        
