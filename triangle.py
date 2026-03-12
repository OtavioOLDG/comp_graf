import glfw
from OpenGL.GL import *
import math

p1 = (-0.5, 0)
p2 = (0.5, 0)
p3 = (0, 0.5)

v = (p2[0] - p1[0], p2[1] - p1[1])

def point(alfa: float, p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]):
    x = alfa * p2[0] + (1 - alfa) * p1[0]
    y = alfa * p2[1] + (1 - alfa) * p1[1]
    return (x, y)

def pointBeta(alfa: float, beta: float, p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]):
    x = (beta * alfa * p2[0]) + (beta * (1 - alfa) * p1[0]) + ((1 - beta) * p3[0])
    y = (beta * alfa * p2[1]) + (beta * (1 - alfa) * p1[1]) + ((1 - beta) * p3[1])

    return (x,y)

def init():
    glClearColor(1, 1, 1, 1)
    glShadeModel(GL_SMOOTH)

def render():
    glClear(GL_COLOR_BUFFER_BIT)

    glPointSize(4) 
    glBegin(GL_POINTS)

    steps = 100 

    for i in range(steps + 1):
        alfa = i / steps
        for j in range(steps + 1):
            beta = j / steps
            
            [x, y] = pointBeta(alfa, beta, p1, p2, p3)

            peso_p1_red = beta * (1 - alfa)
            peso_p2_green = beta * alfa     
            peso_p3_blue = 1 - beta         
            
            glColor3f(peso_p1, peso_p2, peso_p3)
            glVertex2f(x, y)

    glEnd()

def main():
    if not glfw.init():
        return
        
    window = glfw.create_window(800, 600, 'Interpolação de Cores no Triângulo', None, None)
    
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    init()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)
        
    glfw.terminate()

if __name__ == "__main__":
    main()


