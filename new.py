# TODO
'''
    - Normalização
    - Consistência da Janela do Dispositivo (Display/win)
    - Interface Gráfica

'''
from graphics   import *
from math       import *
from sys        import *
import calculos

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
            arestaaux = [int(s) for s in a[i].split(",") if s.isdigit()]
            arestas.append(arestaaux)
        else:
            surfaux = [int(s) for s in a[i].split(",") if s.isdigit()]
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

def draw(w, arestas, P):
    for i in range(0, len(arestas[0])):
        x = P[0][arestas[0][i]]/P[3][arestas[0][i]]
        y = P[1][arestas[0][i]]/P[3][arestas[0][i]]
        p1 = Point(x, y)

        x = P[0][arestas[1][i]]/P[3][arestas[1][i]]
        y = P[1][arestas[1][i]]/P[3][arestas[1][i]]
        p2 = Point(x, y)

        line = Line(p1, p2)

        line.setFill('white')
        line.draw(w)

def draw2(w, arestas, P):
    for i in range(0, len(arestas[0])):
        x = (-1) * P[0][arestas[0][i]]/P[3][arestas[0][i]]
        y = P[1][arestas[0][i]]/P[3][arestas[0][i]]
        p1 = Point(x, y)

        x = (-1) * P[0][arestas[1][i]]/P[3][arestas[1][i]]
        y = P[1][arestas[1][i]]/P[3][arestas[1][i]]
        p2 = Point(x, y)

        line = Line(p1, p2)

        line.setFill('red')
        line.draw(w)

def main():
# DEFAULTs
    display = (300, 300)

    viewC = (4, 4, 10)

    pt1 = (0, 0, 0, 1)
    pt2 = (1, 0, 0, 1)
    pt3 = (0, 1, 0, 1)

    #pers    = True
    pers   = False

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

    op = str(raw_input("Perspectiva? [S/N] "))

    if op == "S":
        pers = True
    else:
        pers = False
   
    if pers:
        Mproj = calculos.matPersp(N, viewC, Ds[2], Ds[0], Ds[1])
    else:
        Mproj = calculos.matPar(N, viewC, Ds[0], Ds[1])
    
    # Matriz P'
    P = calculos.mMatrizes(Mproj, v)
    
    # InitTela
    win = GraphWin(f, display[0], display[1])
    win.setBackground('black')
    win.setCoords(-8.0, 8.0, 8.0, -8.0)

    # Desenha
    draw2(win, a, P)
    win.getMouse()

main()
