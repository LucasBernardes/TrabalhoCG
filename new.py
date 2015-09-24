# TODO
'''

    - CALCULAR AS PARADA
    - PLOTAR

'''
from sys        import *
from math       import *
import calculos
import graphics

def leObjeto(name):
    line = open(name, 'r').read()
    a = line.splitlines()
    hasht = 0
    vertices    = []
    arestas     = []
    superficies = []

    for i in range (0, len(a)):
        if a[i] == "#":
            hasht += 1
        elif (hasht == 0):
            verticeaux = [float(s) for s in a[i].split(",") if s.isdigit()]
            vertices.append(verticeaux)
        elif (hasht == 1):
            arestaaux = [float(s) for s in a[i].split(",") if s.isdigit()]
            arestas.append(arestaaux)
        else:
            surfaux = [float(s) for s in a[i].split(",") if s.isdigit()]
            superficies.append(surfaux)

    return vertices, arestas, superficies

def leParam():
    ponto1  = [0.0, 0.0, 0.0]
    ponto2  = [0.0, 0.0, 0.0]
    ponto3  = [0.0, 0.0, 0.0]
    C       = [0.0, 0.0, 0.0]

    print("Ponto de Vista (C):")
    C[0] = float(input("A: "))
    C[1] = float(input("B: "))
    C[2] = float(input("C: "))
    print()

    print("Plano de projecao:")
    print("Ponto 1:")
    ponto1[0] = float(input("x: "))
    ponto1[1] = float(input("y: "))
    ponto1[2] = float(input("z: "))
    
    print("Ponto 2:")
    ponto2[0] = float(input("x: "))
    ponto2[1] = float(input("y: "))
    ponto2[2] = float(input("z: "))

    print("Ponto 3:")
    ponto3[0] = float(input("x: "))
    ponto3[1] = float(input("y: "))
    ponto3[2] = float(input("z: "))
    print()

    ans = input("[PER]spectiva ou [PRO]jetiva?: ")
    if (ans == "PER"):
        per = 1
    else:
        per = 0

    return C, ponto1, ponto2, ponto3, per

def draw(arestas, P):
    for a in arestas:
        Line(Point(P[a[0]][0], P[a[0]][1]), Point(P[a[1]][0], P[a[1]][1]))

def main():
# DEFAULTs
    display = (400, 300)

    viewC = (0, 0, 0)

    pt1 = (0, 0, 0, 1)
    pt2 = (1, 0, 0, 1)
    pt3 = (1, 1, 0, 1)

    pers = 1

# Program
    f = str(raw_input("Nome do arquivo de objeto: "))
    v, a, s = leObjeto(f)

    #Params default
    #viewC, pt1, pt2, pt3, pers = leParam()

    # Calculo do vetor normal
    N = calculos.vetorNormal(pt1, pt2, pt3)

    # Calculo dos ds
    Ds = calculos.calculoD(N, pt1, viewC)
    # Ds[0] = d0, Ds[1] = d1, Ds[2] = d

    if pers:
        Mproj = calculos.matPersp(N, viewC, Ds[2], Ds[0])
    else:
        Mproj = calculos.matPar(N, viewC, Ds[0], Ds[1])

    # Matriz P'
    P = calculos.mMatrizes(Mproj, v)

    # InitTela
    GraphWin(filename, display[0], display[1])

    # Desenha
    draw(a, P)

main()
