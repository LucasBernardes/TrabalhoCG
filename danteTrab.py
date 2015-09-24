import pygame
import calculos
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
mat = [[2.6,0,0],[0,1.26,0],[0,0,1]]


def lerArq(nome):
    linestring = open(nome, 'r').read()
    a = linestring.splitlines()
    hasht = 0
    vertice = []
    aresta = []
    for x in range (0,len(a)):
      if a[x] == "#":
        hasht = 1
      elif (hasht == 1):
            arestaaux = [int(s) for s in a[x].split(",") if s.isdigit()]
            vertice.append(arestaaux)
      else:
            vertaux = [int(s) for s in a[x].split(",") if s.isdigit()]
            aresta.append(vertaux)
    glBegin(GL_LINES)
    y = 0
    tam = (len(vertice[0]))

    '''m = calculos.mMatrizes(mat,aresta)
    
    for x in range(0,tam):
        glVertex3fv((m[0][vertice[y][x]],m[1][vertice[y][x]],m[2][vertice[y][x]]))
        glVertex3fv((m[0][vertice[y+1][x]],m[1][vertice[y+1][x]],m[2][vertice[y+1][x]]))

    '''

    for x in range(0,tam):
        glVertex3fv((aresta[0][vertice[y][x]],aresta[1][vertice[y][x]],aresta[2][vertice[y][x]]))
        glVertex3fv((aresta[0][vertice[y+1][x]],aresta[1][vertice[y+1][x]],aresta[2][vertice[y+1][x]]))

    glEnd()



    

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    print(display[0]/display[1])
    gluPerspective(50, float(display[0])/float(display[1]), 0.1, 50.0)

    glTranslatef(-1.0,-1.0,-10.0)
    nomearq = "cubo.txt"
    '''raw_input('Inserir nome do arq: ')'''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        '''Aqui chama o arquivo '''
        
        
        lerArq(str(nomearq))
        pygame.display.flip()
        pygame.time.wait(10)


main()
