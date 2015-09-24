from OpenGL.GL      import *
from OpenGL.GLU     import *
from OpenGL.GLUT    import *
from sys            import *

def drawScene():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 1.0, 1.0)

    # Draw
    glBegin(GL_POLYGON)
    
    glVertex3f(20.0, 20.0, 0.0)
    glVertex3f(80.0, 20.0, 0.0)
    glVertex3f(80.0, 80.0, 0.0)
    glVertex3f(20.0, 80.0, 0.0)

    glEnd()

    glFlush()

def setup():
    glClearColor(0.0, 0.0, 0.0, 0.0)

def resize(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 100.0, 0.0, 100.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def keyInput(key, x, y):
    if (key == 27):
        exit(0)

def main():
    glutInit(argv)

    glutInitContextVersion(4, 3)
    glutInitContextProfile(GLUT_COMPATIBILITY_PROFILE)

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("square.py")
    glutDisplayFunc(drawScene)
    glutReshapeFunc(resize)
    glutKeyboardFunc(keyInput)

    glewExpetimental = GL_TRUE
    glewInit()

    setup()

    glutMainLoop()

main()
