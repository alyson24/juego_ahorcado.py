import random
import time
IMAGENES_AHORCADO = ['''

   +---+
   |   |
       |
       |
       |
       |

=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#Lista de palabras
palabras = ["manzana", "platano", "kiwi", "papaya", "mandarina", "cereza", "sandia","alemania", "italia", "colombia", "venezuela","argentina", "mexico",
          "australia", "chile", "tormenta", "ballena", "avispa", "cuchillo", "circulo", "chimenea", "grupo", "abuelo", "anillo", "autobus", "observatorio"
          "valiente", "dormir", "huesos", "argumentar", "humillante", "escenario", "auditorio", "leon", "sandalia", "oso", "alegria", "antiguo", "album"]

def obtenerPalabraAlAzar(listaDePalabras):
#Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]
 
def mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
    print()
 
    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()
 
    espaciosVacíos = '_' * len(palabraSecreta)
 
    for i in range(len(palabraSecreta)): #completar los espacios vacíos con las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]
 
    for letra in espaciosVacíos: #mostrar la palabra secreta con espacios entre cada letra
        print(letra, end=' ')
    print()
 
def obtenerIntento(letrasProbadas):
#Verificar si el jugador solo ingreso una letra y no otra cosa
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('ERROR INGRESA UNA LETRA')
        else:
            return intento
 
def jugarDeNuevo():
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('¿Quieres jugar de nuevo? (si o no)')
    return input().lower().startswith('s')
 
print('////Bienvenidos al juego del Ahorcado////')
time.sleep(1)
print('El juego consiste en adivinar una palabra letra por letra y solo cuentas con 6 intentos')
time.sleep(1)
print('Empezemos a jugar')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False
 
while True:
    mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
 
#Permite al jugador escribir una letra.
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
 
    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
 
#Verifica si el jugador ha ganado.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print('¡GANASTE!')
            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento
 
#Verificar si el jugador perdio
        if len(letrasIncorrectas) == len(IMAGENES_AHORCADO) - 1:
            mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡PERDISTE! la palabra era "' + palabraSecreta + '"')
            juegoTerminado = True
 
#Preguntar si el jugador quiere volver a jugar
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break
