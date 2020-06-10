import numpy as np
import jsonPy


def buscarPrioridadPrimordial():
    for i in range(int(num)):
        if num_array[i] == 4:
            agregarPrioridadPrimordial(i, 1)
        if num_array[i] == 0:
            agregarPrioridadPrimordial(i, -1)


def agregarPrioridadPrimordial(pos, value):
    agregarLuz(pos - auxNum, value)
    agregarLuz(pos - 1, value)
    agregarLuz(pos + 1, value)
    agregarLuz(pos + auxNum, value)


def poblarMatris(num_array):
    print('Ingresa los datos de la matris: ')
    for i in range(int(num)):
        n = input("valor :")
        if n == '':
            n = None
        else:
            n = int(n)
        num_array.append(n)
    return num_array


def iluminarCordenada(filaI=1, columnaI=1):
    fila = 0
    for i in range(int(num)):  # iluminar fila
        if i % auxNum == 0:
            fila = fila + 1
        if fila == filaI:
            Ivector[i] = 1
            if Ivector[i] != 1:
                Ivector[i] = 1

            else:   # si el vector ya esta iluminado en esa columnaa hay un error y el proyecto fracasó
                print('[ERROR]: el sector no puede eliminarse, fallaste ')
                return False


def iluminar(pos):
    pos=pos+1
    i = 0
    columna = 0
    fila = 1
    for i in range(pos):
        if columna == auxNum:
            columna = 0
        columna = columna + 1
        
        if i != 0 and i != 1:
            if i % auxNum == 0:
                fila = fila + 1

    print('coordenadas  que deben ser iluminadas : ---> fila ',
        fila, 'columna ', columna)
    iluminarArriba(pos - 1,fila) #la idea es recorrer desde la pos en la fila hasta 0 agregando 1's
    iluminarAbajo(pos -1,fila)#la idea es recorrer desde la pos en la fila hasta auxNum  agregando 1's
    iluminarDerecha(pos -1,columna) #la idea es recorrer desde la pos en la columna hasta auxNum agregando 1's 
    iluminarIzquierda(pos -1,columna)#la idea es recorrer desde la pos en la columna hasta 0 agregando 1's

    # aca se tiene que iluminar entonces arriba abajo izquierda y derecha

def iluminarArriba(pos, fila):#* provamos con una de 4x4 en la pos = 10
    if fila < 0:
        i = fila
        for i in range(fila,0,-1):
            print('iluminando arriba')
            if num_array[pos] == None or num_array[pos] == 1:
                Ivector[pos] = 1
                print(pos)
            else:
                break
            pos = pos - auxNum


def iluminarAbajo(pos, fila):  # * provamos con una de 4x4 en la pos = 10
    i = fila
    for i in range(fila, auxNum +1 ):
        if num_array[pos] == None or num_array[pos] == 1:
            print (pos)
            Ivector[pos ] = 1
        else:
            break
        pos = pos + auxNum


def iluminarIzquierda(pos, columna):  # * provamos con una de 4x4 en la pos = 10
    i = columna
    for i in range(columna, 0, -1):
        if num_array[pos] == None or num_array[pos] == 1:
            print(i)
            Ivector[pos] = 1
        else:
            break
        pos = pos - 1

#! no funciona bien
def iluminarDerecha(pos, columna):  # * provamos con una de 4x4 en la pos = 10
    i = columna
    for i in range(columna, auxNum + 1):
        print('poos',pos)
        print('iluminando der')
        if num_array[pos] == None or num_array[pos] == 1:
            Ivector[pos] = 1
        else:
            break
        pos = pos + 1

def agregarLuzCordenadas(filaL=2, columnaL=2):
    pos = columnaL + (filaL - 1) * auxNum
    Lvector[pos - 1] = 1


def agregarLuz(pos, value):
    if pos>= 0 and pos <= num: #* solo se agrega luz dentro de los limites
        print('aca no deve entrar una posicion menor a 0', pos)
        Lvector[pos] = value
        if value == 1: #* si no es un valor de restriccion 
            iluminar(pos)


def guardarEnJson(tablero):
    item = {'tablero': tablero}
    jsonPy.addItem(currJson, dic, item)


# ___________________________PROGRAMA__________________________________________________
currJson = 'registro'
dic = 'tablerosPrueba'

if jsonPy.findJson(currJson):
    print('allready exist a json')
else:
    jsonPy.addNewJson(currJson)

aux = input("De que dimencion deceas tu matris ? :")
auxNum = int(aux)
num = int(aux)
num = num*num  # Dimencion de espacios de la matris

num_array = list()
# Vector de espacios iluminados 1-> iluminado / 0-> no iluminado
Ivector = np.zeros(num,dtype=int)
# Vector de espacios cun luz 1-> conLuz / 0-> no sin luz/ None -> imposible poner luz
Lvector = np.zeros(num,dtype=int)


num_array = poblarMatris(num_array)

opcion = input('Quieres guardar este tablero ? [y/n]    ')
if opcion == 'y':
    guardarEnJson(num_array)

print('Vector problema:', num_array)
print('Vector iluminacion:', Ivector)
print('Vector luz:', Lvector)
buscarPrioridadPrimordial()
print('Vector luz:', Lvector)
print('Vector iluminacion:', Ivector)
