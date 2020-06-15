import numpy as np
import jsonPy

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

def buscarPrioridadPrimordial():
    for i in range(int(num)):
        if num_array[i] == 0:
            agregarLuzPrimordial(i, -1)
        if num_array[i] == 4:
            agregarLuzPrimordial(i, 1)
#! si hay un 2 y esta en una esquina


def agregarLuzPrimordial(pos, value ):

    if limiteArriba(pos):
        print('no se agrega a la derecha')
    else:
        agregarLuz(pos - auxNum, value)
    if limiteIzquierda(pos):
        print('no se agrega a la Izquierda')
    else:
        agregarLuz(pos - 1, value)
    if limiteDerecha(pos):
        print('no se agrega a la derecha')
    else:
        agregarLuz(pos + 1, value)
    if limiteAbajo(pos):
        print('no se agrega a la derecha')
    else:
        agregarLuz(pos + auxNum, value)


def agregarLuzSecundaria(pos, value, numeroElemento):
    espaciosLibres = {
        'arriba': False,
        'abajo': False,
        'derecha': False,
        'izquierda': False,
    }

    espaciosLibresCantidad = 0

    if limiteArriba(pos):
        print('no se agrega a la derecha')
    else:
        espaciosLibres['arriba'] = True
    if limiteIzquierda(pos):
        print('no se agrega a la Izquierda')
    else:
        espaciosLibres['izquierda'] = True
    if limiteDerecha(pos):
        print('no se agrega a la derecha')
    else:
        espaciosLibres['derecha'] = True
    if limiteAbajo(pos):
        print('no se agrega a la derecha')
    else:
        espaciosLibres['abajo'] = True

    for libres in espaciosLibres:
        if libres:
            espaciosLibresCantidad = espaciosLibresCantidad + 1
    if numeroElemento == espaciosLibresCantidad:
        print('se deberia poner una ampolleta en cada espacio libre segun corresponda')


def limiteDerecha(pos):#! abria comprobar como con limite si hay un bloque negro en alguno de los lados que se revisa
    fila, columna = getCordenadas(pos)
    if columna == auxNum:
        print('limite derecha si')
        return True
    else:
        print('limite derecha no')
        return False

def limiteIzquierda(pos):
    fila, columna = getCordenadas(pos)
    if columna == 1:
        print('si')
        return True
    else:
        print('no')
        return False

def limiteAbajo(pos):
    fila, columna = getCordenadas(pos)
    if fila == auxNum:
        print('si')
        return True
    else:
        print('no')
        return False

def limiteArriba(pos):
    fila, columna = getCordenadas(pos)
    if fila == 1:
        print('si')
        return True
    else:
        print('no')
        return False

def agregarLuz(pos, value):
    if pos >= 0 and pos <= num:  # * solo se agrega luz dentro de los limites
        Lvector[pos] = value
        if value == 1:  
            iluminar(pos)


def iluminar(pos):
    fila , columna = getCordenadas(pos)
    # la idea es recorrer desde la pos en la fila hasta 0 agregando 1's
    iluminarArriba(pos , fila)
    # la idea es recorrer desde la pos en la fila hasta auxNum  agregando 1's
    iluminarAbajo(pos , fila)
    # la idea es recorrer desde la pos en la columna hasta auxNum agregando 1's
    iluminarDerecha(pos , columna)
    # la idea es recorrer desde la pos en la columna hasta 0 agregando 1's
    iluminarIzquierda(pos , columna)

def iluminarArriba(pos, fila):  
    if fila > 0:
        i = fila
        for i in range(fila, 0, -1):
            print('iluminando arriba')
            if num_array[pos] == None or num_array[pos] == 1:
                    Ivector[pos] = 1
            else:
                break
            print(' se rompio el iluminar arriba por que hay un ',
                  num_array[pos], 'en la pos', pos + 1)
            pos = pos - auxNum

def iluminarAbajo(pos, fila):  
    i = fila
    for i in range(fila, auxNum + 1):
        if num_array[pos] == None or num_array[pos] == 1:
                Ivector[pos] = 1
        else:
            break
        pos = pos + auxNum

def iluminarIzquierda(pos, columna):  
    i = columna
    for i in range(columna, 0, -1):
        if num_array[pos] == None or num_array[pos] == 1:
                Ivector[pos] = 1
        else:
            break
        pos = pos - 1

def iluminarDerecha(pos, columna):  
    i = columna
    for i in range(columna, auxNum + 1):
        if num_array[pos] == None or num_array[pos] == 1:
                Ivector[pos] = 1
        else:
            break
        pos = pos + 1





    # aca se tiene que iluminar entonces arriba abajo izquierda y derecha


def getCordenadas(pos):
    pos = pos+1
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
    return fila , columna

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
