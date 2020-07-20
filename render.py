from utilidades import *

def color(r, g, b):
    return bytes([round(b * 255), round(g * 255), round(r * 255)])

BLACK = color(0,0,0)
WHITE = color(1,1,1)
YELLOW = color(1,1,0)

class render(object):

    def __init__(self):
        self.width = 0
        self.height = 0
        self.default_color = BLACK
        self.vetex_color = WHITE
        self.pixels = []
        self.xVP=0
        self.yVP = 0
        self.widthVP = 0
        self.heightVP = 0

    def glInit(self):
        self.iniciarFramebuffer(BLACK)

    def glCreateWindow(self, w, h):
        self.width = w
        self.height = h
        self.iniciarFramebuffer(BLACK)


    def iniciarFramebuffer(self, c):
        self.pixels = []
        for y in range(self.height):
            linea=[]
            for x in range(self.width):
                linea.append(c)
            self.pixels.append(linea)

        #print(str(self.pixels))


        #self.pixels = [ [ BLACK for x in range(self.width)] for y in range(self.height) ]

    def glViewPort(self, x, y, width, height):
        self.xVP= x
        self.yVP = y
        self.widthVP = width
        self.heightVP = height

    def glClear(self):
        self.iniciarFramebuffer(self.default_color)

    def glClearColor(self, r, g, b):
        self.default_color=color(r, g, b)

    def glVertex(self, x, y):
        #pos X
        xIMG = self.xVP + (x+1)* (self.widthVP/2)
        #pos Y
        yIMG = self.yVP + (y+1)*(self.heightVP / 2)

        self.pintarPixelIMG(round(xIMG),round(yIMG))

        #print("x: "+str(xIMG))
        #print("y: " + str(yIMG))


    def pintarPixelIMG(self, x, y):
        #print("x->" + str(x))
        #print("y->" + str(y))
        self.pixels[y][x] = self.vetex_color

    def glColor(self, r, g, b):
        self.vetex_color=color(r, g, b)

    def glFinish(self):
        self.generar("gotham.bmp")

    def generar(self, filename):

        imagen = open(filename, 'wb')

        #BITMAPFILEHEADER
        #14 Bytes

        imagen.write(bytes('B'.encode('ascii')))
        imagen.write(bytes('M'.encode('ascii')))
        imagen.write(dword(14+40+ self.width * self.height * 3))  #4
        imagen.write(word(0)) #2
        imagen.write(word(0)) #2
        imagen.write(dword(14+40)) #4

        #BITMAPINFOHEADER
        #40 Bytes

        imagen.write(dword(40)) #4
        imagen.write(dword(self.width)) #4
        imagen.write(dword(self.height)) #4
        imagen.write(word(1)) #2
        imagen.write(word(24)) # 2
        imagen.write(dword(0)) # 4
        imagen.write(dword(self.width * self.height * 3))  # 4

        imagen.write(dword(0))  # 4
        imagen.write(dword(0))  # 4
        imagen.write(dword(0))  # 4
        imagen.write(dword(0))  # 4

        #self.pixels[11][11]=color(162,0,255)

        for y in range(self.height):
            for x in range(self.width):
                imagen.write(self.pixels[y][x])

        imagen.close()


    def glLine(self, x0, y0, x1, y1):
        # x0: x inicial de la linea
        x0 = self.xVP + (x0 + 1) * (self.widthVP / 2)
        # x1: x final de la linea
        x1 = self.xVP + (x1 + 1) * (self.widthVP / 2)
        # y0: y inicial de la linea
        y0 = self.yVP + (y0 + 1) * (self.heightVP / 2)
        # y1: y final de la linea
        y1 = self.yVP + (y1 + 1) * (self.heightVP / 2)




