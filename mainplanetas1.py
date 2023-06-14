#Declaramos bibliotecas
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
#Se piden los datos de velocidad inicial y el ángulo
vi=float(input("Digita la velocidad inicial: "))
angulo=math.radians(int(input("Digita el angulo: ")))
gravedad=[9.81,3.71,24.79,10.44,8.87,11.15,3.7,274,0.62]#tierra,marte,jupiter,saturno,venus y urano,neptuno, mercurio, sol, pluton
#Funciones que permiten determinar la posicion de la particula en un tiempo dentro de la funcion
def x_pos(angulo,t,vi):
    x=vi*np.cos(angulo)*t
    return x

def y_pos(angulo,t,vi,g):
    y=(vi*np.sin(angulo)*t)-((g*t**2)/2)
    return y
#funcion que calcula la altura, el alcance y el tiempo de vuelo de la particula
def calcular(vi,angulo,g):
    print("Gravedad: ",g)
    alcance=((vi**2)*math.sin(2*angulo))/g
    tiempo=(2*vi*math.sin(angulo))/g
    altura=((vi**2)*(math.sin(angulo))**2)/(2*g)
    print("Alcance: ",alcance)
    print("Tiempo: ",tiempo)
    print("Altura: ",altura)
    t=np.linspace(0,10,100)
    x=x_pos(angulo,t,vi)
    y=y_pos(angulo,t,vi,g)
    N=len(t)

    fig, ax=plt.subplots()
    ln, = plt.plot(x,y,'ro')
    ax.set_xlim(0,280)
    ax.set_ylim(0,100)
#funcion que crea la animacion del proyectil moviendose por la funcion
    def actualizar(i):
        ln.set_data(x[i],y[i])
        return ln,
    ani = animation.FuncAnimation(fig,actualizar,range(N),interval=0.00001)
    plt.plot(x,y)
    plt.grid()
    plt.show()
#seleccion del planeta para cambiar la gravedad
print("""
    ¿Que en que planeta se va a realizar el tiro?
        1) Mercurio
        2) Venus
        3) Tierra
        4) Marte
        5) Jupiter
        6)Saturno
        7)Urano
        8)Neptuno
        9)pluton
        10)El Sol
        11)Salir
        """)
#casos que se dan en base a la opcion escogida
opcion = int(input("Elige una opción: ") )     
if opcion == 1:
        g=gravedad[6]
        calcular(vi,angulo,g)
elif opcion == 2:
        g=gravedad[4]
        calcular(vi,angulo,g)
elif opcion == 3:
        g=gravedad[0]
        calcular(vi,angulo,g)
elif opcion == 4:
        g=gravedad[1]
        calcular(vi,angulo,g)
elif opcion == 5:
        g=gravedad[2]
        calcular(vi,angulo,g)
elif opcion == 6:
        g=gravedad[3]
        calcular(vi,angulo,g)
elif opcion == 7:
        g=gravedad[4]
        calcular(vi,angulo,g)
elif opcion == 8:
        g=gravedad[5]
        calcular(vi,angulo,g)
elif opcion == 9:
        g=gravedad[8]
        calcular(vi,angulo,g)
elif opcion == 10:
        g=gravedad[7]
        calcular(vi,angulo,g)
elif opcion == 11:
        sys.exit()
else:
        print("Opción incorrecta")