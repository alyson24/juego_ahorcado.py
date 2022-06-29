# juego_ahorcado.py

Juego de Ahorcado 

- Consiste en adivinar una palabra letra por letra 
- El juego cuenta con 6 intentos 
Lo primero que se hizo fue crear el diagrama del ahorcado, después crear una lista con variedad de palabras que son: 
"manzana", "platano", "kiwi", "papaya", "mandarina", "cereza", "sandia","alemania", "italia", "colombia", "venezuela",
"argentina", "mexico","australia", "chile", "tormenta", "ballena", "avispa", "cuchillo", "circulo", "chimenea", "grupo", 
"abuelo", "anillo", "autobus","observatorio", "valiente", "dormir", "huesos", "argumentar", "humillante", "escenario", 
"auditorio", "leon", "sandalia", "oso", "alegria", "antiguo", "album"
- Se creo el diagrama del ahorcado 
- cada vez que pierde el jugador se ira llenado el ahorcado hasta quedar asi:

                    +---+
                    |   |
                    O   |
                   /|\  |
                   / \  |
                        |
                 =========
                 
- El juego escoge una palabra al azar si ponemos letras incorrectas aparecerá todas las letras que pusimos anteriormente. 
- En el caso volvamos a poner una letra que ya elegimos el juego dira que: Ya has probado esa letra. Elige otra.
- El programa no permite poner números o símbolos solo esta programado para poner letras.
- Al terminar el juego en el caso si ganaste aparecerá “¡GANASTE!” y si perdiste aparece la palabra secreta mas “¡PERDISTE!”
- Despues el juego preguntara al jugador si queremos volver a jugar 

Implementación

Al juego se le implemento dos cosas:
-	Jugar con la computadora
-	Jugar dos juagares

La primera implementación consiste en que se creó dos listas de opciones y pistas, ejemplo:

Opción: pavo
Pista: navidad y comida
La computadora te dirá cuantas letras contiene la palabra elegida te dará dos pistas, el jugador debe de ir adivinando letra por letra.

La segunda implementación consiste en que el jugador 1 elige cualquier palabra y debe de escribir tres pistas, el jugador dos debe de adivinar la palabra con la ayuda de las tres pistas.

Las dos formas de jugar ahorcado cuentan con 6 intentos y no se puede escribir números o signos.

