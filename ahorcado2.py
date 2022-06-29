import random
import sys

def main():
    print("        Juego Ahorcado")
    print("Menu de opciones")
    print("1. Jugar contra la Computadora")
    print("2. Jugar con dos jugadores")
    print("3. Salir")
    
    while True:
        opcion = int(input("Escoge la opcion deseada: "))
        if opcion != 1 and opcion != 2 and opcion != 3:
            continue
        else:
            break

    if opcion == 1:
        opcion1()

    elif opcion == 2:
        opcion2() 
    
    elif opcion ==3:
        print("¡Gracias por jugar, hasta luego!")
        sys.exit()

def opcion1 ():
    opciones = ["manzana", "cine", "bicileta", "medico", "lluvia", "pavo", "tierra", "oceano", 
            "cama", "futbol", "telefono", "navidad", "reloj", "guitarra", "fuego", "cuadro",
            "planeta", "fotografia", "afeitarse"]
    pista = [ ["fruta", "rojo"],
            ["pantalla", "pelicula"],
            ["ciclista", "montar"],
            ["hospital", "curar"],
            ["agua", "cielo"],
            ["navidad", "comida"],
            ["planeta", "vida"],
            ["agua", "extenso"],
            ["comodo", "dormir"],
            ["deporte", "patear balón"],
            ["móvil", "llamar"],
            ["celebracion", "diciembre"],
            ["hora", "números"],
            ["instrumento","cuerdas"],
            ["quemar", "lleña"],
            ["retrato", "museo"],
            ["grande","astronomico"],
            ["albúm", "camara"],
            ["barba", "cuchilla"]]
               
    palabra = random.choice(opciones)  
    indice_palabra = opciones.index(palabra)  
    palabra_tapada = [] 
    separador = ""
    intentos = 6
    
    print("¡BIENVENIDO A AHORCADO CONTRA LA COMPUTADORA!")
    print("Instrucciones: El sistema escogera una palabra y te dara dos pistas para adivinar la palabra")
    print("Tu trabajo es ir adivinando las letras que componen la palabra")
    print("Si te equivocas en la letra mas de "+ str(intentos)+" veces, perderas el juego.")

    for i in range (len(palabra)): 
        palabra_tapada.append("_") 
    
    while True:
        print("")
        ahorcado(intentos)
        print("")
        for i in range (len(palabra)):
            print(palabra_tapada[i],end =" ")   
        print("Tu palabra tiene: "+str(len(palabra))+ " letras") 
        print("Tus pista son:  " + pista[indice_palabra][0])
        print("                 " + pista[indice_palabra][1])
    
        print("Escribe una letra: ")
        
        if separador.join(palabra_tapada) == palabra:
            print("Felicidades !GANASTE!")
            main()
    
        guess = input("Respuesta: ")  
        guess = guess.lower()
        
        if guess == palabra: 
            main()
        
        elif guess in palabra: 
            for i in range(len(palabra)): 
                if palabra[i] == guess:
                    indice_string = palabra.index(guess)
                    palabra_tapada[i] = palabra[i]
                    
            print("¡Sigue asi!")
            continue 
                   
        elif guess not in palabra:
            print("¡INCORRECTO!")
            if intentos == 0: 
                print("¡PERDISTE!")
                print( "+------+")
                print( "|      |")
                print( "|      O")
                print( "|     /|\ ")
                print( "|     / \ ")
                print( "|        ")
                print("===========")
                print("Tu palabra era: "+palabra)
                main()
            
            print("INTENTOS RESTANTES: "+str(intentos-1)) 
            intentos = intentos -1 
            continue 

def opcion2():
    palabra_tapada = [] 
    separador = ""
    pista_conteo = 3
    intentos = 6
    
    print("=====¡BIENVENIDO A AHORCADO 1 VS 1!=====")
    print("Instrucciones: Los dos jugadores se deben nombrar como Jugador 1 y Jugador 2.")
    print("El Jugador 1 debera escoger una palabra y 3 pistas")
    print("EL trabajo del Jugador 2 es ir adivinando las letras de la palabra")
    print("Si el Jugador 2 se equivoca  en la letra mas de "+ str(intentos)+" veces, perdera el juego y gana el Jugador 1.")
    print("Si el Jugador 2 adivina la palabra completa ganara el juego y perdera el Jugador 1.")
    print("")
    print("Jugador 1 escriba la palabra")
    print("")
    palabra = input("Palabra por adivinar: ")
    pista = [0]* 3
    
    for i in range(len(pista)):
        pista[i] = input("Pista "+str(i+1)+": ")
    
    print("=========================================================================================================")
    print("=========================================================================================================")
    
    print("¡JUGADOR 2 NO VEAS MAS ARRIBA DE ESTA LINEA!")
    
    print("¡JUGADOR 2 PUEDE EMPEZAR A ADIVINAR!")
    
    for i in range (len(palabra)): 
        palabra_tapada.append("_") 
    
    while True:
        ahorcado(intentos)
        for i in range (len(palabra)):
            print(palabra_tapada[i],end =" ")   
        print("Tu palabra tiene: "+str(len(palabra))+ " letras") 
        print("Tus pistas son: "+ pista[0])
        print("                " + pista[1])
        print("                " + pista[2])
    
        print("Puedes escribir: ")
        
        if separador.join(palabra_tapada) == palabra:
            print("Felicidades Jugador 2. !GANASTE!")
            main()
    
        guess = input("Respuesta: ")  
        guess = guess.lower()
        
        if guess == palabra: 
            main()
        
        elif guess in palabra: 
            for i in range(len(palabra)): 
                if palabra[i] == guess:
                    indice_string = palabra.index(guess)
                    palabra_tapada[i] = palabra[i]
                    
            print("¡Sigue asi!")
            continue
         
        elif guess not in palabra: 
            print("¡INCORRECTO!")
            if intentos == 0: 
                print("¡GANA EL JUGADOR 1!")
                print( "X======X")
                print( "|      |")
                print( "|      O")
                print( "|     /|\ ")
                print( "|     / \ ")
                print( "|        ")
                print("===========")
                print("Tu palabra era: "+palabra)
                main()
            
            print("INTENTOS RESTANTES: "+str(intentos-1)) 
            intentos = intentos -1 
            continue 
    
def ahorcado(intentos):
    if intentos == 1:
        print( "X======X")
        print( "|      |")
        print( "|      O")
        print( "|     /|\ ")
        print( "|     /  ")
        print( "|        ")
        print("===========")
    elif intentos == 2:
        print( "X======X")
        print( "|      |")
        print( "|      O")
        print( "|     /|\ ")
        print( "|         ")
        print( "|        ")
        print("===========")
    elif intentos == 3:
        print( "X======X")
        print( "|      |")
        print( "|      O")
        print( "|     /| ")
        print( "|         ")
        print( "|        ")
        print("===========")
    elif intentos == 4:
        print( "X======X")
        print( "|      |")
        print( "|      O")
        print( "|      | ")
        print( "|         ")
        print( "|        ")
        print("===========")
    elif intentos == 5:
        print( "X======X")
        print( "|      |")
        print( "|      O")
        print( "|       ")
        print( "|         ")
        print( "|        ")
        print("===========")
    elif intentos == 6:
        print( "X======X")
        print( "|      |")
        print( "|       ")
        print( "|       ")
        print( "|         ")
        print( "|        ")
        print("===========")
        

main()
