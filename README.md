# 🧠 RESUMEN TAREA AI
[light Up Aplication Lwink](https://es.puzzle-light-up.com/)

## 			📄 CONCEPTOS

**Enfoque en el método** : esto es que se quiere tener el mismo resultado, replicando los pasos que sigue la persona en la obtención de tal resultado. En el caso de el trabajo deben ser las restricciones

**backtraking** : Es un algoritmo que sirve para encontrar soluciones a un problema, por lo general problemas de satisfacción de restricciones, los backtracks son las alternativas que no cumplen con las restricciones planteadas.

## 			📖 TRABAJO

**Resumen del desarrollo**: debemos desarrollar un backtraking, utilizando técnicas de satisfacción de restricciones como en IO.

**Detalles de la implementación**: 

- el algoritmo debe replicar el comportamiento de una persona.

- la agregación de una ampolleta no puede ser modificada,cambiada o eliminada una vez puesta

- deben aplicarse reglas

- el algoritmo debe ser capas de iluminar cualquier tablero de N x N

- no puede utilizar el backtracking( no puede generar y descartar cambios )


## 👓 ABSTRACCIÓN

### MASTRIZ

    BLANK --------------->NONE
    BLOCK ------------>-1
    0 ----------------> 0
    1 ----------------> 1
    2-----------------> 2
    3-----------------> 3
    4-----------------> 4

### MASTRIZ LUZ

	1 -----------> iluminado
	0 -----------> no iluminado
	-1 ------------> restringido

### MARTRIZ ILUMINACION

    se marca las casillas que se iluminan
    1 ----------------> iluminado
    0  ----------------> no iluminado


## ⚠️RESTRICCIONES  

**restricciones generales:** 

se tendra que iluminar solo los sectores desde la luz hasta los bloques negros

![restricGeneral](imgs\restricGeneral.jpg)

Posibles movimientos

![PosibleMov](imgs\PosibleMov.jpg)

restricciones primordiales: prioridad primera



![PosibleMov](imgs\PosibleMov.jpg)

![Restriccion1](imgs\Restriccion1.jpg)



Restricciones de posibilidad: prioridad secundaria

![Restriccion2](imgs\Restriccion2.jpg)



![Restriccion3](imgs\Restriccion3.jpg)

![Restriccion4](imgs\Restriccion4.jpg)

Restricciones de alternativa: prioridad terciaria

![Restriccion5](imgs\Restriccion5.jpg)

![Restriccion6](imgs\Restriccion6.jpg)

![Restriccion7](imgs\Restriccion7.jpg)

