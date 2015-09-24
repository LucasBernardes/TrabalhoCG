import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
matrixVert =[
    [0,2,0,2,0,2,0,2],
    [0,0,2,2,0,0,2,2],
    [0,0,0,0,2,2,2,2]
]

matrixEdge = [
    [0,0,0,1,2,2,3,1,4,4,5,6],
    [1,2,4,3,3,6,7,5,6,5,7,7]
]

edges = (
    (0,1),
    (0,2),
    (0,4),
    (1,3),
    (2,3),
    (2,6),
    (3,7),
    (1,5),
    (4,6),
    (4,5),
    (5,7),
    (6,7)
    )


def Cube():
    glBegin(GL_LINES)
    y = 0
    tam = (len(edges))
    for x in range(0,tam):
        glVertex3fv((matrixVert[0][matrixEdge[y][x]],matrixVert[1][matrixEdge[y][x]],matrixVert[2][matrixEdge[y][x]]))
        glVertex3fv((matrixVert[0][matrixEdge[y+1][x]],matrixVert[1][matrixEdge[y+1][x]],matrixVert[2][matrixEdge[y+1][x]]))
    glEnd()

    

def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(50, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(-1.0,-1.0,-5.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
