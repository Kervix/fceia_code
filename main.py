#!/usr/bin/env python3

# Trabajo Práctico Python
# Materia: Programación II
# Entrega: 24/10/22
# Integrantes del grupo:
#  * Laureano Garbelino G-5894/7
#  * Santiago Vrancovich V-3033/3

def generarTablero() -> list:
    '''
    Función que genera el tablero inicial del juego de 8x8 con las 4 fichas iniciales en el centro.

    Representamos el tablero como una lista formada por 8 listas de longitud 8, las cuales pueden estar
    formadas por String de tipo "espacio en blanco", N o B. En tablero, las listas del 0 al 7 representan las
    filas del 1 al 8, y cada posición de la lista representan una columna de A a H.

    Args:
        None
    Returns:
        Retorna un tablero de 8x8 con las 4 fichas iniciales en el centro en
        forma de lista.
    '''

    tablero = []

    cantidadDeFilas = 0
    while cantidadDeFilas != 8:
        tablero.append([" "] * 8)
        cantidadDeFilas += 1

    tablero[3][3] = "B"
    tablero[3][4] = "N"
    tablero[4][3] = "N"
    tablero[4][4] = "B"

    return tablero

def colorDeFicha(tablero: list, pos: list) -> str:
    '''
    La función determina el color de la ficha en el tablero.
    Representamos pos, como un string, el cual esta formado por una letra de A a H y un numero de 1 a 8
    Args:
        tablero: Argumento de tipo list el cual representa el tablero donde se
        va a buscar la ficha.
        pos: Argumento de tipo lista que representa la posición a buscar en el
        tablero.
    Returns:
        La función retorna un valor de tipo str con el color de la ficha, siendo
        estos "B", "N" o " " para representar una casilla vacía.
    '''
    return tablero[pos[0]][pos[1]]

def casillaVacia(tablero: list, pos: list) -> bool:
    '''
    La función determina si la casilla en el tablero esta vacía.
    Representamos la condición de "casilla vacía" mediante un valor de verdad.
    Args:
        tablero: Argumento de tipo list el cual representa el tablero donde se
        va a buscar la ficha.
        pos: Argumento de tipo lista que representa la posición a buscar en el
        tablero.
    Returns:
        La función retorna un valor de tipo bool el cual nos dice si la casilla
        solicitada esta vacía.
    '''

    return colorDeFicha(tablero, pos) == " "

def traducirPosicion(pos: str) -> list:
    '''
    La función traduce las posiciones formadas por una letra y numero a una
    lista de 2 números, la cual nos permite operar sobre el tablero.
    Representamos como un string pos el cual esta formado por una letra de A a H y un numero de 1 a 8
    Args:
        pos: Argumento de tipo str que representa la posición en el tablero a traducir.
    Returns:
        Una lista de 2 números la cual representa la forma numérica de la
        posición
    '''

    dictLetras = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
    return [int(pos[1])-1, dictLetras[pos[0]]]

def resPos(pos1: list, pos2: list) -> list:
    '''
    La función resta dos posiciones numéricas, no revisa que las posiciones
    existan en el tablero.
    Representamos pos1 y pos2 como dos listas de dos elementos del tipo int
    Args:
        pos1: Argumento de tipo list que representa la primer posición a operar
        pos2: Argumento de tipo list que representa la segunda  posición a operar
    Returns:
        La posición resultante de la resta de las 2 posiciones ingresadas
    '''
    return [pos1[0]-pos2[0], pos1[1]-pos2[1]]

def sumPos(pos1: list, pos2: list) -> list:
    '''
    La función suma dos posiciones numéricas, no revisa que las posiciones
    existan en el tablero.
    Representamos pos1 y pos2 como listas de dos elementos del tipo int
    Args:
        pos1: Argumento de tipo list que representa la primer posición a operar
        pos2: Argumento de tipo list que representa la segunda  posición a operar
    Returns:
        La posición resultante de la suma de las 2 posiciones ingresadas
    '''
    return [pos1[0]+pos2[0], pos1[1]+pos2[1]]

def enTablero(pos: str) -> bool:
    '''
    La función determina si la posición esta adentro del rango del tablero.
    Representamos la condición de si una ficha esta en el tablero como un valor de tipo booleano
    Args:
        pos: Argumento de tipo str que representa la posición a validar si esta
        dentro del rango del tablero.
    Returns:
        Retorna un valor del tipo booleano que representa si se encuentra o no
        en el tablero
    '''

    letras = {"A","B","C","D","E","F","G","H"}

    # Revisa que el segundo carácter sea valido intentando convertirlo a un int,
    # en caso de falla, no es una posición que exista dentro del tablero, siendo
    # que el segundo carácter de la posición debe ser un numero entero

    try:
        int(pos[1])
    except:
        return False

    return (pos[0] in letras) and (1 <= int(pos[1]) <= 8)

def posNumericaEnTablero(pos: list) -> bool:
    '''
    La función determina si la posición esta adentro del rango del tablero.
    Representamos la condición de si una ficha esta en el tablero como un valor
    de tipo booleano.
    Args:
        pos: Argumento de tipo list que representa la posición a validar si esta
        dentro del rango del tablero.
    Returns:
        Retorna un valor del tipo booleano que representa si se encuentra o no
        en el tablero
    '''
    return (0 <= pos[0] <= 7) and (0 <= pos[1] <= 7)

def posicionesAlrededor(pos: list) -> list:
    '''
    La función determina todas las posiciones que estén adentro del tablero y
    que rodeen a pos.
    Representamos posiciones como una lista vacía o de listas de listas
    formadas por dos int, de máximo 8 elementos.
    Args:
        pos: Argumento de tipo list que representa la posición central de la
        cual se buscaran las posiciones alrededor.
    Returns:
        Retorna una lista con todas las posicione1s posibles que estén adentro
        del tablero y que rodeen a pos
    Ejemplo:
        pos: [2, 2]
        return:
            [1, 1], [1, 2], [1, 3],
            [2, 1],         [2, 3],
            [3, 1], [3, 2], [3, 3]
    '''

    posiciones = []

    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            # Se revisa que x e y no sean 0 siendo que en este caso nos estaría
            # dando la misma posición que ingresamos
            if posNumericaEnTablero(sumPos(pos, (x, y))) and not (x == 0 and y == 0):
                posiciones.append(sumPos(pos, (x, y)))

    return posiciones

def fichasParaVoltear(tablero: list, pos: list, color: str) -> list:
    '''
    La función determina si hay flanqueos posibles a partir de la ficha
    indicada.
    Representamos las fichas a voltear como una de lista de listas de 2 elementos del tipo
    int.
    Args:
        tablero: Argumento de tipo list que representa el tablero de juego actual
        pos: Argumento de tipo list que representa la posición en el tablero a
        revisar.
        color: Argumento de tipo str que representa el color de la ficha en la
        jugada
    Returns:
        Retorna una lista con todas las fichas a voltear en los posibles
        flanqueos, en caso de que no exista ninguno devuelve una lista vacía
    '''

    posiciones = []

    # Revisa si la casilla donde se intenta poner la ficha esta vacía, en caso
    # de que no lo estuviera no existen jugadas posibles siendo que no se puede
    # poner la ficha en una posición ya ocupada por otra ficha

    if not casillaVacia(tablero, pos):
        return []

    # Revisa las posiciones alrededor de la ficha y solo revisa si hay un
    # flanqueo posible en las direcciones donde las fichas tengan un color
    # opuesto al de la ficha que esta realizando la jugada

    for fichaPosible in posicionesAlrededor(pos):
         if colorDeFicha(tablero, fichaPosible) == colorContrario(color):
            # Se determina hacia donde debería avanzar la búsqueda y se guardan
            # la ficha de donde partimos y la ficha primer ficha del color
            # opuesto que ya encontramos previamente
            tendencia = resPos(fichaPosible, pos) # Indica la dirección hacia donde tenemos que avanzar
            posibleRecta = []
            nuevaPos = fichaPosible
            posibleRecta.append(pos) # Se guarda la posición de la ficha que ingresamos
            posibleRecta.append(nuevaPos) # Se guarda la ficha aledaña que encontramos del color opuesto

            # Avanzar hasta encontrar un elemento de nuestro color o un espacio en blanco
            while colorDeFicha(tablero, nuevaPos) == colorContrario(color) and posNumericaEnTablero(sumPos(nuevaPos, tendencia)):
                nuevaPos = sumPos(nuevaPos, tendencia)
                posibleRecta.append(nuevaPos)

            # Si el ultimo elemento que encontramos es de nuestro color, es una
            # posición valida, caso contrario de si es un espacio en blanco se descarta la posición
            if colorDeFicha(tablero, nuevaPos) == color:
                for i in posibleRecta:
                    posiciones.append(i)

    return posiciones

def ponerFicha(tablero: list, pos: list, color: str) -> list:
    '''
    La función cambia el color de la ficha solicitada, sin revisar si existe en el tablero
    Representamos el tablero como una lista de listas las cuales contienen strings
    Args:
        tablero: Argumento de tipo list que representa el tablero de juego actual
        pos: Argumento de tipo list que representa la posición en el tablero a
        cambiar de color.
        color: Argumento de tipo str que representa a que color se debe cambiar
        la ficha
    Returns:
        Retorna un nuevo tablero donde la ficha se cambio de color
    '''
    tablero[pos[0]][pos[1]] = color
    return tablero

def colorContrario(colorOriginal: str) -> str:
    '''
    La función determina el color de ficha opuesto al que recibe como argumento.
    Representamos el color con un string en la forma "B" o "N"
    Args:
        colorOriginal: Argumento de tipo str que representa un color de ficha
    Returns:
        Retorna el color opuesto a la ficha que recibe como argumento
    '''
    colores = {"N":"B","B":"N"}
    return colores[colorOriginal]

def pisarLista(listaAnidada: list) -> list:
    '''
    La función convierte una lista de listas a una lista de un solo nivel, esta función hace
    lo que comúnmente se conoce como "ArrayFlatten".
    Representamos la salida como una lista.
    Args:
        listaAnidada: Argumento de tipo list que representa una lista anidada
    Returns:
        Retorna todos los elementos de una lista anidada en una nueva lista
        con todos los elementos a mismo nivel
    '''
    listaPlana = []
    for elemento in listaAnidada:
        if type(elemento) == list or type(elemento) == tuple:
            for items in elemento:
                listaPlana.append(items)
        else:
            listaPlana.append(elemento)

    return listaPlana

def obtenerArchivo() -> str:
    '''
    La función pide al usuario un nombre de archivo y verifica que el mismo sea valido, en
    en caso de que no lo sea se vuelve a pedir hasta que se ingrese un nombre de archivo valido
    Representamos a la salida de la función como un string, el cual va a ser el
    nombre del archivo.
    Args:
        None
    Returns:
        Retorna el nombre y ruta del archivo en forma de str
    '''
    archivo = input("Ingrese la dirección del archivo: ")
    nombreValido = False

    while not nombreValido:
        try:
            if open(archivo,"r"):
                nombreValido = True
        except:
            archivo = input("Dirección invalida, ingrese nuevamente la dirección del archivo: ")

    return archivo

def main() -> None:
    '''
    La función lee un archivo donde se encuentre una partida de Othello e
    interpreta el resultado de esa partida, el resultado sera mostrado por
    pantalla indicando, puntajes, estado del tablero y quien seria el ganador.
    En caso de que haya un error en esta partida se notificara en que linea del
    archivo se encuentra este error y el estado del tablero antes de esa jugada.
    Args:
        None
    Returns:
        None
    '''
    # Se generan los valores iniciales para el juego
    archivo = open(obtenerArchivo(),"r")
    tablero = generarTablero()
    error = False

    # Obtiene los valores sobre el nombre de los jugadores y su color, ademas
    # del color inicial de la partida

    primerJugador = archivo.readline().strip()
    segundoJugador = archivo.readline().strip()
    colorJugada = archivo.readline().strip()

    nombresJugadores = [primerJugador[:-2], segundoJugador[:-2]]
    colorJugadores = [primerJugador[-1:], segundoJugador[-1:]]

    # Comienza a leer la primera linea de jugadas en el archivo
    nuevaLinea = archivo.readline()
    numeroDeLinea = 3 # Las 3 primeras lineas son de los jugadores y color inicial, por lo que nuestro contador parte del 3

    while nuevaLinea != "" and not error:
        # Elimina caracteres innecesarios como espacios o \n
        posOriginal = nuevaLinea.strip()

        # Previene leer EOF o espacios en blanco, los cuales se tienen que saltar
        if len(posOriginal) == 2 and enTablero(posOriginal):
            posTraducida = traducirPosicion(posOriginal)

            # Revisa si existen flanqueos posibles, en caso de que no existan se
            # genera un error para indicar en que linea sucede
            flanqueos = fichasParaVoltear(tablero, posTraducida, colorJugada)
            if flanqueos != []:
                for ficha in flanqueos:
                    tablero = ponerFicha(tablero, ficha, colorJugada)
            else:
                error = True

        # Revisa si el string es vacío o tiene espacios, si no cumple con esto
        # da un error, esto funciona siendo que un string vacío devuelve el
        # valor False y como ya utilizamos la función strip() anteriormente si
        # el string es puramente espacios nos va a devolver un string vacío

        elif posOriginal:
            error = True

        # Avanzar a la nueva linea
        nuevaLinea = archivo.readline()
        colorJugada = colorContrario(colorJugada)
        numeroDeLinea += 1

    # Mostrar el tablero ,de una forma visual una vez que ya se termino de
    # interpretar la partida
    print("\n      A   B   C   D   E   F   G   H")
    print(" "*3, "+---"*8 + "+"," "*3)

    for contador, fichas in enumerate(tablero):
        print(" ",contador + 1, "|", end=" ")
        print(*fichas, sep=" | ", end="")
        print(" |",contador + 1)
        print(" "*3, "+---"*8 + "+"," "*3)

    print("      A   B   C   D   E   F   G   H")

    # Obtener el puntaje basándose en la cantidad de fichas de cada color en el tablero
    tableroPisado = pisarLista(tablero)
    puntajeJugadores = [tableroPisado.count(colorJugadores[0]), tableroPisado.count(colorJugadores[1])]

    # Muestra el nombre de cada jugador junto a su cantidad de fichas
    print("\n \u001b[34mPuntajes:\u001b[0m\n ",
            "•",nombresJugadores[0]+":", puntajeJugadores[0],"\n ",
            "•",nombresJugadores[1]+":", puntajeJugadores[1])

    # En caso de error, se muestra cual es la linea que genera el error, sino se muestra el ganador
    # de la partida o empate si fuera el caso
    if error:
        print("\n\u001b[31m [x] Error:\u001b[0m Posicion invalida en linea", numeroDeLinea)
    elif puntajeJugadores[0] == puntajeJugadores[1]:
        print("\n\u001b[32m [✓] Partida valida:\u001b[0m es un empate\n")
    elif puntajeJugadores[0] > puntajeJugadores[1]:
        print("\n\u001b[32m [✓] Partida valida:\u001b[0m", nombresJugadores[0], "es el ganador \n")
    else:
        print("\n\u001b[32m [✓] Partida valida:\u001b[0m", nombresJugadores[1], "es el ganador \n")

    archivo.close()

if __name__ == '__main__':
   main()
