import numpy as np
import jsonPy

#? probar

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
    treses = []
    doses = []
    unos = []
    
    print(' 1️⃣ Analizando restricciones primordiales: prioridad primera ...')
    for i in range(int(num)):
        if num_array[i] == 0:
            agregarLuzPrimordial(i, -1, 0)
    for i in range(int(num)):
        if num_array[i] == 4:
            agregarLuzPrimordial(i, 1, 4)

    print(' 2️⃣ Analizando restricciones de posibilidad: prioridad secundaria ...')
    for i in range(int(num)):
        if num_array[i] == 3:
            treses.append(i)
    agregarLuzSecundaria(treses, 1, 3)

    for i in range(int(num)):
        if num_array[i] == 2:
            doses.append(i)
    
    agregarLuzSecundaria(doses, 1, 2)

    for i in range(int(num)):
        if num_array[i] == 1:
            unos.append(i)

    agregarLuzSecundaria(unos, 1, 2)


def rellenaEspacios():
    print('🆙 Rellenamos los espacios ')
    i=0
    for i in range(0,num) :
        if Lvector[i] == 0 and Ivector[i] == 0 :
            agregarLuz(i,1)

    



def agregarLuzPrimordial(pos, valor, numeroElemento):
    cantidadLimites = 0
    if limiteArriba(pos):
        cantidadLimites = cantidadLimites + 1
        if( 4 - numeroElemento < cantidadLimites ):

            return False
    else:
        agregarLuz(pos - auxNum, valor)
    if limiteIzquierda(pos):
        cantidadLimites = cantidadLimites + 1
        if(4 - numeroElemento < cantidadLimites):

            return False
    else:
        agregarLuz(pos - 1, valor)
    if limiteDerecha(pos):
        cantidadLimites = cantidadLimites + 1
        if(4 - numeroElemento < cantidadLimites):

            return False
    else:
        agregarLuz(pos + 1, valor)
    if limiteAbajo(pos):
        cantidadLimites = cantidadLimites + 1
        if(4 - numeroElemento < cantidadLimites):

            return False
    else:
        agregarLuz(pos + auxNum, valor)


def agregarLuzSecundaria(poss, valor, numeroElemento): 

    datos = [] # aca voy a tener todos los datos

    for pos in poss:
        data = componerData(pos,numeroElemento)
        if data != None:
            datos.append(data)



    complete = len(poss)
    while(complete != 0):
        for dato in datos :
            print('     🔁 Analisando espacios optimos en')
            if(dato['cantidadEspaciosDisponibles'] == dato['lucesDisponibles'] ):
                for espacio in dato['espaciosLibres']:
                    agregarLuz(espacio, 1)
                    dato['lucesExistentes'].append(espacio)
                complete = complete - 1
            else:
                print('.')
        datos = []
        for pos in poss:
            data = componerData(pos, numeroElemento)
            if data != None:
                datos.append(data)
        


def notComplete(datos):
    cantidadDatos = len(datos)
    cantidadCompletados = 0
    for dato in datos:
        if (dato['posCompletado']):
            cantidadCompletados = cantidadCompletados + 1
    if (cantidadCompletados == cantidadDatos):
        return False
    else:
        return True


def componerData(pos, numeroElemento):
    print('         🆙 Actualizando el analisis de contexto')
    posCompletado = False
    lucesEncontradas, espaciosLibres = encuentraEspacios(pos, numeroElemento)  # ? retorna un arreglo

    cantidadLucesEncontradas = len(lucesEncontradas)
    cantidadEspaciosDisponibles = len(espaciosLibres)
    if(cantidadEspaciosDisponibles == 0 or cantidadLucesEncontradas == numeroElemento):
        print('☑️ Bloque completado')
        posCompletado = True

    if(cantidadEspaciosDisponibles > numeroElemento):
            return None
    else:
            data = {
                'lucesExistentes': lucesEncontradas,
                'espaciosLibres': espaciosLibres,
                'cantidadEspaciosDisponibles': cantidadEspaciosDisponibles,
                'cantidadDeLucesEncontradas': cantidadLucesEncontradas,
                'lucesDisponibles':  numeroElemento - cantidadLucesEncontradas,
                'posCompletado': posCompletado
            }
    if(posCompletado and cantidadEspaciosDisponibles == 1):
        agregarLuz(espaciosLibres[0], -1)
    return data



def encuentraEspacios(pos,numeroElemento):
    print('         🔎 Buscar espacios ocupados | espacios libre ')
    libres=[]
    ocupado=[]
    cantidadEspaciosLibres = 0
    sinLimite = {
        'arriba' : False,
        'abajo': False,
        'izquierda': False,
        'derecha': False,
    }
    if limiteArriba(pos):
        print('')
    else:
        sinLimite['arriba'] = True
    if limiteIzquierda(pos):
        print('')
    else:
        sinLimite['izquierda'] = True
    if limiteDerecha(pos):
        print('')
    else:
        sinLimite['derecha'] = True
    if limiteAbajo(pos):
        print('')
    else:
        sinLimite['abajo'] = True
    for libre in sinLimite:
        if sinLimite[libre]:
            cantidadEspaciosLibres = cantidadEspaciosLibres + 1

    if numeroElemento != cantidadEspaciosLibres:
        if(sinLimite['arriba']):
            if Lvector[pos - auxNum] == 0 and Ivector[pos - auxNum] == 0:
                libres.append(pos - auxNum)
            if Lvector[pos - auxNum] == 1:
                ocupado.append(pos - auxNum)
        if(sinLimite['izquierda']):
            if Lvector[pos - 1] == 0 and Ivector[pos - 1] == 0:
                libres.append(pos - 1)
            if Lvector[pos - 1] == 1 :
                ocupado.append(pos - 1)
        if(sinLimite['derecha']):
            if Lvector[pos + 1] == 0 and Ivector[pos + 1] == 0:
                libres.append(pos + 1)
            if Lvector[pos + 1] == 1:
                ocupado.append(pos + 1)
        if(sinLimite['abajo']):
            if Lvector[pos + auxNum] == 0 and Ivector[pos + auxNum] == 0:
                libres.append(pos + auxNum)
            if Lvector[pos + auxNum] == 1:
                ocupado.append(pos+ auxNum)
    else :
        print('no podra ser viable, no existe la cantidad exacta de espacios para agregar esa cantidad de luces')
    return ocupado, libres

def limiteDerecha(pos):
    
    fila, columna = getCordenadas(pos)
    if columna == auxNum :
        return True
    else:
        return False 

def limiteIzquierda(pos):
    fila, columna = getCordenadas(pos)
    if columna == 1 :

        return True
    else:
        return False


def limiteAbajo(pos):
    fila, columna = getCordenadas(pos)
    if fila == auxNum :
        return True
    else:
        return False


def limiteArriba(pos): 
    fila, columna = getCordenadas(pos)
    if fila == 1 :
        return True
    else:
        return False

def agregarLuz(pos, valor):
    if pos >= 0 and pos <= num: 
        Lvector[pos] = valor
        if valor == 1:  
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
            if num_array[pos] == None or num_array[pos] == 1:
                    Ivector[pos] = 1
            else:
                break
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

aux = input("📏 De que dimencion deceas tu matris ? [N x N] donde  N : ")
auxNum = int(aux)
num = int(aux)
num = num*num  # Dimencion de espacios de la matris
num_array = list()
# Vector de espacios iluminados 1-> iluminado / 0-> no iluminado
Ivector = np.zeros(num,dtype=int)
# Vector de espacios cun luz 1-> conLuz / 0-> no sin luz/ None -> imposible poner luz
Lvector = np.zeros(num,dtype=int)


num_array = poblarMatris(num_array)

# opcion = input('Quieres guardar este tablero ? [y/n]    ')
# if opcion == 'y':
#     guardarEnJson(num_array)

print('⚪Nuestro vector problema:', *num_array, sep=" | ")
print('⚪Vector iluminacion inicial:', *Ivector, sep=" | ")
print('⚪Vector luz inicial :', *Lvector, sep=" | ")
buscarPrioridadPrimordial()
rellenaEspacios()
print('💡 Vector luz:', *Lvector, sep=" | ")
print(' 🔦 Vector iluminacion:', *Ivector, sep=" | ")
