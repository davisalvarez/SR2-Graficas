"""
UVG
GRAFICAS POR COMPUTADORA - seccion 20

Davis Alvarez - 15842

SR1: Points
"""
from render import *

img = render()

img.glInit() #5
img.glCreateWindow(100,100) #5
img.glClearColor(0.5,1,0.36) #10
img.glClear() #20
img.glViewPort(50,50,48,48) #10
img.glColor(0,0.5,0.5)#15
#img.glVertex(0.75,0.12)#30
img.glVertex(1,1)
img.glVertex(-1,1)
img.glVertex(-1,-1)
img.glVertex(1,-1)
img.glVertex(0,0)
img.glFinish() #5




