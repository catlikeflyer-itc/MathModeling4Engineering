def init_N():
    N = set()
    for i in range(1,50):
        N.add(i)
    return N

def init_A(N):
    A = set()
    for element in N:
        for i in N:
            if((2*i)-1==element):
                if(element>17):
                    A.add(element)
    A = list(A)
    A.sort()
    return A

def init_B(N):
    B = set()
    for element in N:
        for i in N:
            if(2*i==element):
                if(element<38):
                    B.add(element)
    B = list(B)
    B.sort()
    return B

def init_C(N):
    C = set()
    for element in N:
        for i in N:
            if(5*i==element):
                C.add(element)
    C = list(C)
    C.sort()
    return C    

def init_D(N):
    D = set()
    for element in N:
        for i in N:
            if(10*i==element):
                D.add(element)
    D = list(D)
    D.sort()
    return D

def ej_a():
    A_C = set()
    A_C_B = set()
    for element_A in init_A(init_N()):
        A_C.add(element_A)
    for element_C in init_C(init_N()):
        A_C.add(element_C)
    for element_AC in A_C:
        for element_B in init_B(init_N()):
            if (element_AC == element_B):
                A_C_B.add(element_AC)
    A_C_B = list(A_C_B)
    A_C_B.sort()
    return A_C_B

def ej_b():
    B_A_D = set()
    for element_B in init_B(init_N()):
        for element_A in init_A(init_N()):
            for element_D in init_D(init_N()):
                if ((element_A == element_B) and (element_B == element_D) and (element_A == element_D)):
                    B_A_D.add(element_B)
    B_A_D = list(B_A_D)
    B_A_D.sort()
    return B_A_D

def ej_c():
    B_comp = set()
    Bc_A = set()
    Bc_A_C = set()
    for element_B in init_B(init_N()):
        for element_N in init_N():
            if (element_B == element_N):
                continue
            else:
                B_comp.add(element_N)
    for element_A in init_A(init_N()):
        for element_Bc in B_comp:
            if (element_A == element_Bc):
                Bc_A.add(element_A)
    Bc_A = list(Bc_A)
    for element_C in init_C(init_N()):
        for element_BcA in Bc_A:
            if (element_C == element_BcA):
                Bc_A.remove(element_C)
    Bc_A_C = list(Bc_A)
    Bc_A_C.sort()
    return Bc_A_C

def ej_d():
    C_comp = set()
    B_Cc = set()
    A_B_Cc = set()
    for element_C in init_C(init_N()):
        for element_N in init_N():
            if (element_C == element_N):
                continue
            else:
                C_comp.add(element_N)
    for element_B in init_B(init_N()):
        for element_Cc in C_comp:
            if (element_B == element_Cc):
                B_Cc.add(element_B)
    for element_A in init_A(init_N()):
        for element_BCc in B_Cc:
            if (element_BCc == element_A):
                continue
            else:
                A_B_Cc.add(element_A)
    A_B_Cc = list(A_B_Cc)
    A_B_Cc.sort()
    return A_B_Cc

def main():
    N = init_N()
    print("A: {0}".format(init_A(N)))
    print("B: {0}".format(init_B(N)))
    print("C: {0}".format(init_C(N)))
    print("D: {0}".format(init_D(N)))
    print("Ejercicio a): {0}".format(ej_a()))
    print("Ejercicio b): {0}".format(ej_b()))
    print("Ejercicio c): {0}".format(ej_c()))
    print("Ejercicio d): {0}".format(ej_d()))


main()