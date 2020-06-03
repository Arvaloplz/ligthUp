import numpy as np
import jsonPy
# ___________________________FUNCIONES__________________________________________________


def buscarPrioridadPrimordial():
    for i in range(int(num)):
        if num_array[i] == 4:
            agregarPrioridadPrimordial(i, 1)
        if num_array[i] == 0:
            agregarPrioridadPrimordial(i, None)


def agregarPrioridadPrimordial(pos, value):
    agregarLuz(pos - auxNum, value)
    agregarLuz(pos-1, value)
    agregarLuz(pos+1, value)
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
    i = 0
    columna = 0
    fila = 1
    pos = pos + 1
    for i in range(pos):
        if columna == auxNum:
            columna = 0
        columna = columna + 1

        if i != 0 and i != 1:
            if i % auxNum == 0:
                fila = fila + 1

    print('coordenadas  que deben ser iluminadas : ---> fila ',fila, 'columna ', columna)


def agregarLuzCordenadas(filaL=2, columnaL=2):
    pos = columnaL + (filaL - 1) * auxNum
    Lvector[pos - 1] = 1


def agregarLuz(pos, value):
    Lvector[pos] = value
    if value != None:
        iluminar(pos)


def guardarEnJson(tablero):
    item= {'tablero':tablero}
    jsonPy.addItem(currJson,dic,item)


# ___________________________PROGRAMA__________________________________________________
currJson = 'registro'
dic = 'tableros'
jsonPy.addNewJson(currJson)
jsonPy.addField(currJson,dic)
aux = input("De que dimencion deceas tu matris ? :")
auxNum = int(aux)
num = int(aux)
num = num*num  # Dimencion de espacios de la matris

num_array = list()
# Vector de espacios iluminados 1-> iluminado / 0-> no iluminado
Ivector = np.zeros(num)
# Vector de espacios cun luz 1-> conLuz / 0-> no sin luz/ None -> imposible poner luz
Lvector = np.zeros(num)


num_array = poblarMatris(num_array)

opcion = input('Quieres guardar este tablero ? [y/n]    ')
if opcion == 'y':
    guardarEnJson(num_array)

print('Vector problema:', num_array)
print('Vector iluminacion:', Ivector)
print('Vector luz:', Lvector)
buscarPrioridadPrimordial()
print('Vector luz:', Lvector)
holamunso