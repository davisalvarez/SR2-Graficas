"""
UVG
GRAFICAS POR COMPUTADORA - seccion 20

Davis Alvarez - 15842

SR1: Points
"""
from render import *

img = render()

img.glInit() #5
img.glCreateWindow(400,400) #5
img.glClearColor(0.5,1,0.36) #10
img.glClear() #20
img.glViewPort(1,1,398,398) #10
img.glColor(0,0.5,0.5)#15
#img.glVertex(0.75,0.12)#30

"""Testear viewport
img.glVertex(1,1)
img.glVertex(-1,1)
img.glVertex(-1,-1)
img.glVertex(1,-1)
img.glVertex(0,0)
"""
"""Testear Linea"""
#primer cuadrante
img.glLine(0,0, 1,0)
img.glLine(0,0, 1,0.1)
img.glLine(0,0, 1,0.2)
img.glLine(0,0, 1,0.3)
img.glLine(0,0, 1,0.4)
img.glLine(0,0, 1,0.5)
img.glLine(0,0, 1,0.6)
img.glLine(0,0, 1,0.7)
img.glLine(0,0, 1,0.8)
img.glLine(0,0, 1,0.9)
img.glLine(0,0, 1,1)
img.glLine(0,0, 0.9,1)
img.glLine(0,0, 0.8,1)
img.glLine(0,0, 0.7,1)
img.glLine(0,0, 0.6,1)
img.glLine(0,0, 0.5,1)
img.glLine(0,0, 0.4,1)
img.glLine(0,0, 0.3,1)
img.glLine(0,0, 0.2,1)
img.glLine(0,0, 0.1,1)
img.glLine(0,0, 0,1)

#primer cuadrante
img.glLine(0,0, -1,0)
img.glLine(0,0, -1,0.1)
img.glLine(0,0, -1,0.2)
img.glLine(0,0, -1,0.3)
img.glLine(0,0, -1,0.4)
img.glLine(0,0, -1,0.5)
img.glLine(0,0, -1,0.6)
img.glLine(0,0, -1,0.7)
img.glLine(0,0, -1,0.8)
img.glLine(0,0, -1,0.9)
img.glLine(0,0, -1,1)
img.glLine(0,0, -0.9,1)
img.glLine(0,0, -0.8,1)
img.glLine(0,0, -0.7,1)
img.glLine(0,0, -0.6,1)
img.glLine(0,0, -0.5,1)
img.glLine(0,0, -0.4,1)
img.glLine(0,0, -0.3,1)
img.glLine(0,0, -0.2,1)
img.glLine(0,0, -0.1,1)
img.glLine(0,0, -0,1)

#primer cuadrante
img.glLine(0,0, 1,-0)
img.glLine(0,0, 1,-0.1)
img.glLine(0,0, 1,-0.2)
img.glLine(0,0, 1,-0.3)
img.glLine(0,0, 1,-0.4)
img.glLine(0,0, 1,-0.5)
img.glLine(0,0, 1,-0.6)
img.glLine(0,0, 1,-0.7)
img.glLine(0,0, 1,-0.8)
img.glLine(0,0, 1,-0.9)
img.glLine(0,0, 1,-1)
img.glLine(0,0, 0.9,-1)
img.glLine(0,0, 0.8,-1)
img.glLine(0,0, 0.7,-1)
img.glLine(0,0, 0.6,-1)
img.glLine(0,0, 0.5,-1)
img.glLine(0,0, 0.4,-1)
img.glLine(0,0, 0.3,-1)
img.glLine(0,0, 0.2,-1)
img.glLine(0,0, 0.1,-1)
img.glLine(0,0, 0,-1)

#primer cuadrante
img.glLine(0,0, -1,-0)
img.glLine(0,0, -1,-0.1)
img.glLine(0,0, -1,-0.2)
img.glLine(0,0, -1,-0.3)
img.glLine(0,0, -1,-0.4)
img.glLine(0,0, -1,-0.5)
img.glLine(0,0, -1,-0.6)
img.glLine(0,0, -1,-0.7)
img.glLine(0,0, -1,-0.8)
img.glLine(0,0, -1,-0.9)
img.glLine(0,0, -1,-1)
img.glLine(0,0, -0.9,-1)
img.glLine(0,0, -0.8,-1)
img.glLine(0,0, -0.7,-1)
img.glLine(0,0, -0.6,-1)
img.glLine(0,0, -0.5,-1)
img.glLine(0,0, -0.4,-1)
img.glLine(0,0, -0.3,-1)
img.glLine(0,0, -0.2,-1)
img.glLine(0,0, -0.1,-1)
img.glLine(0,0, -0,-1)

"""
img.glLine(0,0, -1,0)
img.glLine(0,0, 1,0)
img.glLine(0,0, 0, 1)
img.glLine(0,0, 1,0)
img.glLine(0,0, 1, 0)
"""

img.glFinish() #5




