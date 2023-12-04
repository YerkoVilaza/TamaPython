import time
import random
import os
from colorama import init, Fore, Back, Style
from run_chess import jugarajedrez

init()
#Se agregara un timer que mientras pas tiempo si tocar el tamago se le iran subiendo los estados

#arregla la interfaz, termina de arreglar la interfaz de las acciones
#ponle una interfaz mejorada a la selecion de acciones

#Actividades adicionales: Agrega más opciones de actividades que el Tamagotchi pueda realizar
#como pasear, ver televisión, jugar a otro juego, etc.

#Minijuegos: Crea minijuegos adicionales que el jugador pueda jugar con el 
#Tamagotchi para ganar monedas virtuales o aumentar el estado de felicidad del Tamagotchi.
#Arregla el tema del ajedrez

###########################
class Tamagotchi:
    def limpiar_interfaz(self):
        if os.name == 'nt':  # self.limpiar_interfaz()
            _ = os.system('cls')
        else:
            print('')

    def __init__(self, nombre):
        self.nombre = nombre
        self.sueno = 0
        self.hambre = 0
        self.sed = 0
        self.peso = 0 #
        self.suciedad = 0
        self.aburrimiento = 0
        self.felicidad = 0 #
        self.corazones = 10
        self.curas_disponibles = 3
        self.coins = 1
        self.coins_win = 0
        self.comida = 1
        self.agua = 1

        self.timer = 0
###################################
    def mostrar_estados(self):

        print("|Estado actual de ",end="")
        print("{0: <30}".format(self.nombre)+"  |")
        print("|-------------------------------------------------|")
        print("| hearts:  |   ", end="")
        print("{:<10s}".format(" ❤️ " * self.corazones), "    |")
        print("|-------------------------------------------------|")
        print(Fore.CYAN +"| Sueño:   |", end="")
        print("{:<10s}".format("#" * (self.sueno // 10)), "|", end="")
        print(Fore.RED +"Aburrimiento: |", end="")
        print("{:<10s}".format("#" * (self.aburrimiento // 10)), "|")
        print(Fore.YELLOW +"| Hambre:  |", end="")
        print("{:<10s}".format("#" * (self.hambre // 10)), "|", end="")
        print(Fore.BLUE +"Sed:          |", end="")
        print("{:<10s}".format("#" * (self.sed // 10)), "|")
        print(Fore.GREEN +"| Suciedad:|", end="")
        print("{:<10s}".format("#" * (self.suciedad // 10)), "|", end="")
        print(Fore.MAGENTA +"Peso:         |", end="")
        print("{:<10s}".format("#" * (self.peso // 10)), "|")
        print(Fore.YELLOW +"| Coins:   |", end="")
        print("{:<10s}".format(str(self.coins)), "|", end="")
        print(Fore.RED +"curas:        |", end="")
        print("{:<10s}".format(str(self.curas_disponibles)), "|")
        print(Style.RESET_ALL +"|-------------------------------------------------|")

    def mostrar_estados_maximos(self):
        estados_maximos = []
        if self.sueno == 90:
            estados_maximos.append("sueño")
        if self.hambre == 90:
            estados_maximos.append("hambre")
        if self.suciedad == 90:
            estados_maximos.append("suciedad")
        if self.aburrimiento == 90:
            estados_maximos.append("aburrimiento")

        if estados_maximos:
            print("¡Cuidado!, estados llegando al máximo nivel:")
            for estado in estados_maximos:
                print("-", estado)

    def establecer_todo_al_maximo(self):
            self.sueno = 100
            self.hambre = 100
            self.sed = 100
            self.peso = 100
            self.suciedad = 100
            self.aburrimiento = 100
            print("¡Todos los estados han sido establecidos al máximo nivel!")
###################################################
    def actualizar_corazones(self):
        if self.sueno == 100 or self.hambre == 100 or self.suciedad == 100:
            self.corazones -= 1
            if self.corazones <= 0:
                self.corazones = 0

    def esta_vivo(self):
        return self.corazones > 0
    
    def sanar(self):
        if self.curas_disponibles > 0:
            if self.corazones < 10:
                self.corazones = min(self.corazones + 5, 10)
                self.curas_disponibles -= 1
                print("¡Has sanado a", self.nombre, "y ahora tiene", self.corazones, "corazones!")
            else:
                print(self.nombre, "ya tiene todos los corazones llenos.")
        else:
            print("No tienes más curas disponibles.")
################################################
    def dibujar_perro(self):
        print("|                                                 |")
        print("|                       /\__/\                    |")
        print("|                      / O  O \                   |")
        print("|                      V\  Y /V                   |")
        print("|                       / -  \\                    |")
        print("|                      /     |                    |")
        print("|                     V__)  ||                    |")
        print("|                                                 |")
        
    def dibujar_gato(self):
        print("|                                                 |")
        print("|                       /\\_/\\                     |")
        print("|                      ( ^-^ )                    |")
        print("|                       > - <                     |")
        print("|                      /  _  \\                    |")
        print("|                                                 |")

    def dibujar_raton(self):
        print("|                                                 |")
        print("|                         _._                     |")
        print("|                        |   `                    |")
        print("|                      .-'                        |")
        print("|                   ___|__                        |")
        print("|                  /       \\                      |")
        print("|                  |( )_( )|                      |")
        print("|                   \\{o o}/                       |")
        print("|                    =\\o/=                        |")
        print("|                    ^   ^                        |")
        print("|                                                 |")

#########################################
    def dibujar_perro_jugando(self):
        print("|                                                 |")
        print("|                       /\__/\                    |")
        print("|                      / O  O \                   |")
        print("|                      V\  Y /V                   |")
        print("|                       / -  \\                    |")
        print("|                      /     |                    |")
        print("|                     V__)  || ⚽                 |")
        print("|                                                 |")
        
    def dibujar_gato_jugando(self):
        print("|                                                 |")
        print("|                       /\_/\                     |")
        print("|                      ( ^-^ )                    |")
        print("|                       > - <                     |")
        print("|                   🧶 /  _  \/                   |")
        print("|                                                 |")

    def dibujar_raton_jugando(self):
        print("|                                                 |")
        print("|                         _._                     |")
        print("|                        |   `                    |")
        print("|                      .-'                        |")
        print("|                   ___|__                        |")
        print("|                  /       \\                      |")
        print("|                  |( )_( )|                      |")
        print("|                   \\{o o}/                       |")
        print("|                    =\\o/=                        |")
        print("|                    ^🎲^                         |")
        print("|                                                 |")

#########################################
    def dibujar_perro_esperando(self):
        print("|                   /\__/\                        |")
        print("|                  / O  O \ . . .                 |")
        print("|                  V\  Y /V                       |")
        print("|                   / -  \\                        |")
        print("|                  /     |                        |")
        print("|                 V__)  ||                        |")
    def dibujar_perro_comiendo(self):
        print("|                  /\__/\                         |")
        print("|                 / ^  ^ \                        |")
        print("|                 V\  Y /V                        |")
        print("|                  / -  \\                         |")
        print("|                 /     |                         |")
        print("|                V__)  || 🥩                      |")
    def dibujar_perro_bebiendo(self):
        print("|                 /\__/\                          |")
        print("|                / ^  ^ \                         |")
        print("|                V\  Y /V                         |")
        print("|                 / -  \\                          |")
        print("|                /     |                          |")
        print("|               V__)  || 🍵                       |")

    def dibujar_gato_esperando(self):
        print("|                     /\_/\                       |")
        print("|                    ( -o- ). . .                 |")
        print("|                     > - <                       |")
        print("|                    /  _  \/                     |")
    def dibujar_gato_comiendo(self):
        print("|                     /\_/\                       |")
        print("|                    ( ^o^ )🐟                    |")
        print("|                     > - <                       |")
        print("|                    /  _  \/                     |")
    def dibujar_gato_bebiendo(self):
        print("|                     /\_/\                       |")
        print("|                    ( ^o^ )🧃                    |")
        print("|                     > - <                       |")
        print("|                    /  _  \/                     |")

    def dibujar_raton_esperando(self):
        print("|                        _._                      |")
        print("|                       |   `                     |")
        print("|                     .-'                         |")
        print("|                  ___|__                         |")
        print("|                 /       \\                       |")
        print("|                 |( )_( )|                       |")
        print("|                  \\{o o}/ . . .                  |")
        print("|                   =\\o/=                         |")
        print("|                    ^  ^                         |")
    def dibujar_raton_comiendo(self):
        print("|                        _._                      |")
        print("|                       |   `                     |")
        print("|                     .-'                         |")
        print("|                  ___|__                         |")
        print("|                 /       \\                       |")
        print("|                 |( )_( )|                       |")
        print("|                  \\{^ ^}/                        |")
        print("|                   =\\o/=                         |")
        print("|                    ^🧀^                         |")
    def dibujar_raton_bebiendo(self):
        print("|                       _._                       |")
        print("|                      |   `                      |")
        print("|                    .-'                          |")
        print("|                 ___|__                          |")
        print("|                /       \\                        |")
        print("|                |( )_( )|                        |")
        print("|                 \\{^ ^}/                         |")
        print("|                  =\\o/=                          |")
        print("|                   ^🧉^                          |")
#########################################
    def dibujar_perro_bañandose(self):
        print("|                                                 |")
        print("|                       /\__/\  🚿                |")
        print("|                      / ^  ^ \                   |")
        print("|                      V\  Y /V                   |")
        print("|                       / -  \\                    |")
        print("|                      /     |                    |")
        print("|                     V__)  ||                    |")
        print("|                                                 |")

    def dibujar_gato_bañandose(self):
        print("|                                                 |")
        print("|                       /\\_/\\🚿                   |")
        print("|                      ( ^-^ )                    |")
        print("|                       > - <                     |")
        print("|                      /  _  \\                    |")
        print("|                                                 |")

    def dibujar_raton_bañandose(self):
        print("|                                                 |")
        print("|                         _._                     |")
        print("|                        |   `                    |")
        print("|                      .-'                        |")
        print("|                   ___|__                        |")
        print("|                  /       \\                      |")
        print("|                  |( )_( )| 🚿                   |")
        print("|                   \\{o o}/                       |")
        print("|                    =\\o/=                        |")
        print("|                    ^   ^                        |")
        print("|                                                 |")
#########################################
    def dibujar_perro_estudy(self):
        print("|                                                 |") 
        print("|                       /\__/\  3+3               |") 
        print("|                      / x  x \  0/0=0            |")
        print("|                      V\  Y /V                   |")
        print("|                       / -  \\                    |")
        print("|                      /     |                    |")
        print("|                     V__)  ||                    |")
        print("|                                                 |")

    def dibujar_gato_estudy(self):
        print("|                                                 |")
        print("|                       /\\_/\\ 1+1                 |")
        print("|                      ( x-x ) 5*5                |")
        print("|                       > - <                     |")
        print("|                      /  _  \\                    |")
        print("|                                                 |")

    def dibujar_raton_estudy(self):
        print("|                                                 |")
        print("|                         _._                     |")
        print("|                        |   `                    |")
        print("|                      .-'                        |")
        print("|                   ___|__                        |")
        print("|                  /       \\                      |")
        print("|                  |( )_( )|                      |")
        print("|                   \\{o o}/                       |")
        print("|                    =\\o/=                        |")
        print("|                     ^📖^                        |")
        print("|                                                 |")
#########################################
    def dibujar_perro_mimir(self):
        print("   /\__/\   z")
        print("  / -  - \ z")
        print("  V\  Y /V")
        print("   / -  \\")
        print("  /     |")
        print(" V__)  ||")

    def dibujar_gato_mimir(self):
        print(" /\_/\   z")
        print("( -.- ) z")
        print(" > - < ")
        print("/  _  \/")

    def dibujar_raton_mimir(self):
        print("       _._ ")
        print("      |   `")
        print("    .-' ")
        print(" ___|__")
        print("/       \\")
        print("|( )_( )|  z")
        print(" \\{- -}/ z")
        print("  =\\o/=")
        print("   ^  ^")
#########################################

#########################################
    def gotofuera(self, tamagotchi):
        print("caminando")
        while True:
            self.actualizar_corazones()
            print("Elige a donde iras")
            print("1-juegos")
            print("2-tienda")
            print("3-volver")
            
            opcion_salida = input("[")
            
            if opcion_salida == "1":
                print("juegos")
                tamagotchi.Gamestation()
                time.sleep(1)
            elif opcion_salida == "2":
                tamagotchi.tienda()
                time.sleep(1)
            elif opcion_salida == "3":
                print("volviendo")
                break
            else:
               print("no existe esa opcion")
    def tienda(self):
        print("Bienvenido a la tienda")
        while True:
            print("Que deseas comprar?")
            print("(Tienes un total de: ", self.coins, ")")
            print("[Comida = 10 coins, Agua = 10 coins, Curaciones = 1000 coins]")
            print("1-Comida"+" (tienes:",self.comida, ")")
            print("2-Agua"+" (tienes:", self.agua, ")")
            print("3-Curaciones"+" (tienes:", self.curas_disponibles, ")")
            print("4-Salir")

            opcion_compra = input("[")

            if opcion_compra == "1":
                if self.coins > 10:
                    print("comida")
                else:
                    print("no tienes dinero suficiente")
                    print('')
            elif opcion_compra == "2":
                if self.coins > 10:
                    print("agua")
                else:
                    print("no tienes dinero suficiente")
                    print('')
            elif opcion_compra == "3":
                if self.coins > 1000:
                    print("medicina")
                else:
                    print("no tienes dinero suficiente")
                    print('')
            elif opcion_compra == "4":
                print("saliendo")
                print('')
                break
            else:
                print("no existe esa opcion")
                print('')
    def Gamestation(self):
        while True:
            print(f"Bienvenido a GameStation")
            time.sleep(1)
            self.actualizar_corazones()
            print("\nElige un juego:")
            print("1. Piedra, papel, tijera")
            print("2. Adivina el número")
            print("3. Adivina la palabra")
            print("4. Ajedrez")
            print("5. Salir del arcade")

            opcion_juego = input("Ingresa el número del juego que deseas jugar: ")

            if opcion_juego == "1":
                self.jugar_piedra_papel_tijera()
                self.sueno = min(self.sueno + random.randint(10, 30), 100)
                self.hambre = min(self.hambre + random.randint(20, 40), 100)
                self.suciedad = min(self.suciedad + random.randint(30, 60), 100)
                self.aburrimiento = max(self.aburrimiento - random.randint(10, 20), 0)
                self.felicidad = max(self.felicidad - random.randint(10, 20), 0)
            elif opcion_juego == "2":
                self.jugar_adivina_numero()
                self.sueno = min(self.sueno + random.randint(10, 30), 100)
                self.hambre = min(self.hambre + random.randint(20, 40), 100)
                self.suciedad = min(self.suciedad + random.randint(30, 60), 100)
                self.aburrimiento = max(self.aburrimiento - random.randint(10, 20), 0)
                self.felicidad = max(self.felicidad - random.randint(10, 20), 0)
            elif opcion_juego == "3":
                self.jugar_adivinar_palabra()
                self.sueno = min(self.sueno + random.randint(10, 30), 100)
                self.hambre = min(self.hambre + random.randint(20, 40), 100)
                self.suciedad = min(self.suciedad + random.randint(30, 60), 100)
                self.aburrimiento = max(self.aburrimiento - random.randint(10, 20), 0)
                self.felicidad = max(self.felicidad - random.randint(10, 20), 0)
            elif opcion_juego == "4":
                jugarajedrez()
                self.sueno = min(self.sueno + random.randint(10, 30), 100)
                self.hambre = min(self.hambre + random.randint(20, 40), 100)
                self.suciedad = min(self.suciedad + random.randint(30, 60), 100)
                self.aburrimiento = max(self.aburrimiento - random.randint(10, 20), 0)
                self.felicidad = max(self.felicidad - random.randint(10, 20), 0)
            elif opcion_juego == "5":
                print("\nSaliendo de gamestation...")
                time.sleep(2)
                break
            else:
                print("Opción inválida. Inténtalo de nuevo.")
#######################
    def jugar_piedra_papel_tijera(self):
        print("\n¡Juguemos a Piedra, papel, tijera!")
        print("Elige una opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")

        opcion_jugador = input("[")
        opcion_computadora = random.choice(["1", "2", "3"])

        print("Tu elección:", opcion_jugador)
        print(f"{self.nombre} a elegido:", opcion_computadora)

        if opcion_jugador == opcion_computadora:
            print("Empate")
        elif (opcion_jugador == "1" and opcion_computadora == "3") or \
             (opcion_jugador == "2" and opcion_computadora == "1") or \
             (opcion_jugador == "3" and opcion_computadora == "2"):
            print("¡Ganaste! -10")
            self.aburrimiento = max(self.aburrimiento - 10, 0)
            self.coins_win = min(self.coins_win + random.randint(2, 8), 100)
            print("Coins ganadas: ",self.coins_win)
            self.coins = (self.coins + self.coins_win)
        else:
            print("Perdiste! +10")
            self.aburrimiento = min(self.aburrimiento + 10, 100) #lo hago orgulloso?
########################
    def jugar_adivina_numero(self):
        print("\n¡Juguemos a Adivina el número!")
        print("Estoy pensando en un número del 1 al 10. Adivina cuál es.")

        numero_secreto = random.randint(1, 10)
        intentos = 0
        adivinado = False

        while not adivinado:
            intento = input("Ingresa tu intento: ")

            if intento.isdigit():
                intento = int(intento)
                intentos += 1

                if intento == numero_secreto:
                    print("¡Felicitaciones! Adivinaste el número en", intentos, "intentos.")
                    self.aburrimiento = max(self.aburrimiento - 30, 0)
                    self.coins_win = min(self.coins_win + random.randint(5, 20), 100)
                    print("Coins ganadas: ",self.coins_win)
                    self.coins = (self.coins + self.coins_win)
                    adivinado = True
                elif intento < numero_secreto:
                    print("El número es mayor. Intenta de nuevo.(+10)")
                    self.aburrimiento = min(self.aburrimiento + 10, 100)
                else:
                    print("El número es menor. Intenta de nuevo.(+10)")
                    self.aburrimiento = min(self.aburrimiento + 10, 100)
            else:
                print("Entrada inválida. Ingresa un número válido.")
#######################
    def jugar_adivinar_palabra(self):
        palabras = ["gato", "perro", "pelota", "casa", "sol","pato","piedra","agua",
                    "santotomas","avion","animal","raton","perro","izquierda","juguete",
                    "youtube","teclado","celular","amor","xd","espacio","sorpresa",
                    "mercurio","venus","tierra","marte","jupiter","saturno","urano","neptuno","pluton"
                    "estrella","aire","fuego","terra","computador","palabra","python"]
        jugar_otra_vez = True

        while jugar_otra_vez:
            palabra_secreta = random.choice(palabras)
            letras_adivinadas = set()
            intentos = 10

            print("¡Bienvenido al juego de Adivinar la Palabra!")
            print("Tienes 10 intentos para adivinar la palabra.")
            print("La palabra tiene", len(palabra_secreta), "letras.")

            while intentos > 0:
                print("\nPalabra:", self.mostrar_palabra(palabra_secreta, letras_adivinadas))
                letra = input("Ingresa una letra: ").lower()

                if letra in letras_adivinadas:
                    print("Ya has adivinado esa letra. Intenta con otra.")
                elif letra in palabra_secreta:
                    letras_adivinadas.add(letra)
                    if self.palabra_completa(palabra_secreta, letras_adivinadas):
                        print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
                        self.aburrimiento = max(self.aburrimiento - 30, 0)
                        self.coins_win = min(self.coins_win + random.randint(5, 20), 100)
                        print("Coins ganadas: ",self.coins_win)
                        self.coins = (self.coins + self.coins_win)
                        break
                else:
                    intentos -= 1
                    print("La letra no está en la palabra. Te quedan", intentos, "intentos.")
                    self.aburrimiento = min(self.aburrimiento + 10, 100)

            if intentos == 0:
                print("\n¡Lo siento! No has adivinado la palabra. La palabra era:", palabra_secreta)
                self.aburrimiento = min(self.aburrimiento + 10, 100)

            respuesta = input("\n¿Quieres jugar con otra palabra? (s/n): ")
            if respuesta.lower() != "s":
                jugar_otra_vez = False

    def mostrar_palabra(self, palabra, letras_adivinadas):
        resultado = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                resultado += letra + " "
            else:
                resultado += "_ "
        return resultado.strip()

    def palabra_completa(self, palabra, letras_adivinadas):
        return all(letra in letras_adivinadas for letra in palabra)
################################################
#agrega como iniciar el agredez directamente aqui
################################################
    def alimentar(self,tipo,tamagotchi):
        while True:
            if tipo == "1":
                tamagotchi.dibujar_perro_esperando()
                print("\n")
            elif tipo == "2":
                tamagotchi.dibujar_gato_esperando()
                print("\n")
            elif tipo == "3":
                tamagotchi.dibujar_raton_esperando()
                print("\n")
            print(f"Estas alimentando a {self.nombre}")
            print("Hambre:", self.hambre, "[" + "#" * (self.hambre // 10) + "]")
            print("Sed:", self.sed, "[" + "#" * (self.sed // 10) + "]")
            print("Peso:", self.peso, "[" + "#" * (self.peso // 10) + "]")
            time.sleep(1)
            self.actualizar_corazones()
            print("\nQue le daras a tu mascota:")
            print("1. Comida"+" (tienes:",self.comida, ")")
            print("2. Agua"+" (tienes:", self.agua, ")")
            print("3. Nada, salir de la cocina")

            opcion_comida = input(".")
            print("\n")

            if opcion_comida == "1" and self.aburrimiento < 100:
                
                if self.comida > 0:
                    self.comida = (self.comida - 1)

                    self.sueno = min(self.sueno + random.randint(10, 30), 100)
                    self.hambre = max(self.hambre - random.randint(30, 50), 0)
                    self.suciedad = min(self.suciedad + random.randint(10, 20), 100)
                    self.aburrimiento = min(self.aburrimiento + random.randint(10, 20), 100)
                    print("\n")
                    print(f"{self.nombre} esta comiendo")
                    if tipo == "1":
                        tamagotchi.dibujar_perro_comiendo()
                        print("\n")
                    elif tipo == "2":
                        tamagotchi.dibujar_gato_comiendo()
                        print("\n")
                    elif tipo == "3":
                        tamagotchi.dibujar_raton_comiendo()
                        print("\n")
                    time.sleep(5)
                    self.actualizar_corazones()
                else:
                    print("no tienes comida, compra comida")
            elif opcion_comida == "2" and self.aburrimiento < 100:

                if self.agua > 0:

                    self.agua = (self.agua -1)

                    self.sueno = min(self.sueno + random.randint(10, 30), 100)
                    self.sed = max(self.sed - random.randint(30, 50), 0)
                    self.suciedad = min(self.suciedad + random.randint(10, 20), 100)
                    self.aburrimiento = min(self.aburrimiento + random.randint(10, 20), 100)
                    print("\n")
                    print(f"{self.nombre} esta bebiendo agua")
                    if tipo == "1":
                        tamagotchi.dibujar_perro_bebiendo()
                    elif tipo == "2":
                        tamagotchi.dibujar_gato_bebiendo()
                    elif tipo == "3":
                        tamagotchi.dibujar_raton_bebiendo()
                    time.sleep(5)
                    self.actualizar_corazones()
                else:
                    print("No tienes agua, ve a comprar")
            elif opcion_comida == "3":
                break
            else:
                print("No comere o bebere, estoy aburrido.")
######################################################
    def limpiar(self, tipo, tamagotchi):
        if self.aburrimiento < 100:
            self.sueno = min(self.sueno + random.randint(10, 30), 100)
            self.hambre = min(self.hambre + random.randint(10, 20), 100)
            self.suciedad = max(self.suciedad - random.randint(50, 100), 0)
            self.aburrimiento = min(self.aburrimiento + random.randint(10, 20), 100)
            print(f"Estás limpiando a {self.nombre}")
            time.sleep(5)
            self.actualizar_corazones()
        else:
            print("No quiero bañarme, estoy aburrido.")
##########################################################
    def estudiar(self, tipo, tamagotchi):
        if self.aburrimiento < 100:
            self.sueno = min(self.sueno + random.randint(20, 40), 100)
            self.hambre = min(self.hambre + random.randint(10, 20), 100)
            self.suciedad = min(self.suciedad + random.randint(10, 20), 100)
            self.aburrimiento = min(self.aburrimiento + random.randint(30, 50), 100)
            print(f"Estás estudiando con {self.nombre}")
            time.sleep(5)
            self.actualizar_corazones()
        else:
            print("No quiero estudiar, estoy aburrido.")
##########################################################
    def dormir(self, tipo, tamagotchi):
        if self.aburrimiento < 100:
            self.sueno = max(self.sueno - random.randint(50, 100), 0)
            self.hambre = min(self.hambre + random.randint(10, 20), 100)
            self.suciedad = min(self.suciedad + random.randint(10, 20), 100)
            print(f"{self.nombre} está durmiendo")
            time.sleep(10)
            self.actualizar_corazones()
        else:
            print("No puedo dormir, estoy aburrido.")
###########################

##########################

###########################
def nombre_tipo(tamagotchi):
    print('Elija un tipo de mascota: 1:perro  2:gato  3:rata.')
    tipo = input("Que mascota quieres?: ")
    nombre = input("Ingresa un nombre para tu animal: ")
    tamagotchi.nombre = nombre
    return tipo, nombre
###########################
def Instrucciones():
        print('--------------------------------------------------------------------------------------')
        print('')
        print('Instrucciones: ')
        print('')
        print(' + Primero debe elegir que tipo de mascota quieres y un nombre para el,')
        print('   se puede elegir entre un perro, un gato o una rata.')
        print('')
        print(' + Luego debe mantener viva a su mascota, para esto debe darle de comer,')
        print('   beber y jugar con ella entre otras opciones.')
        print('')
        print(' + Tenga en cuenta que cada accion que realiza modifica las estadisticas,')
        print('   recuerde estar atento a sus estadisticcas ya que cada 100 de algo negativo')
        print('   a este se le bajara un corazon.')
        print('')
        print(' + Solo tendras 3 curas para el, las otras tendras que comprarlas(son caras!!!)')
        print('')
        print(' + Si llega a 0 corazones su mascota morira y tendra que empezar denuevo')
        print('')
        print(' + Cada tipo de mascota tiene una necesidad especial, el perro requiere jugar mas tiempo,')
        print('   el gato requiere tomar agua mas seguido y la rata requiere comer mas.')
        print('')
        print('--------------------------------------------------------------------------------------')
        print('')

def DejarJuego():
    print('Gracias por jugar.')
##########################
def acciones(tamagotchi,tipo):
    
    while True:
        opcion = input("\n¿Qué acción deseas realizar? \n[1-Jugar] [2-Alimentar] [3-Limpiar]\n[4-Estudiar] [5-dormir] [6-Sanar]\n-")

        if opcion == "1":
            tamagotchi.limpiar_interfaz()
            if tipo == "1":
                tamagotchi.dibujar_perro_esperando()
                print("\n")
            elif tipo == "2":
                tamagotchi.dibujar_gato_esperando()
                print("\n")
            elif tipo == "3":
                tamagotchi.dibujar_raton_esperando()
                print("\n")
            tamagotchi.gotofuera(tamagotchi)
            tamagotchi.limpiar_interfaz()
            print("\n")
            print("regresando...")
            print("\n")
            time.sleep(2)
            tamagotchi.limpiar_interfaz()
        elif opcion == "2":
            tamagotchi.limpiar_interfaz()
            tamagotchi.alimentar(tipo,tamagotchi)
            tamagotchi.limpiar_interfaz()
            print("\n")
            print("regresando...")
            print("\n")
            time.sleep(2)
            tamagotchi.limpiar_interfaz()
        elif opcion == "3":
            tamagotchi.limpiar_interfaz()
            if tipo == "1":
                tamagotchi.dibujar_perro_bañandose()
            elif tipo == "2":
                tamagotchi.dibujar_gato_bañandose()
            elif tipo == "3":
                tamagotchi.dibujar_raton_bañandose()
            tamagotchi.limpiar(tipo,tamagotchi)
            tamagotchi.limpiar_interfaz()
            print("\n")
            print("regresando...")
            print("\n")
            time.sleep(2)
            tamagotchi.limpiar_interfaz()
        elif opcion == "4":
            tamagotchi.limpiar_interfaz()
            if tipo == "1":
                tamagotchi.dibujar_perro_estudy()
            elif tipo == "2":
                tamagotchi.dibujar_gato_estudy()
            elif tipo == "3":
                tamagotchi.dibujar_raton_estudy()
            tamagotchi.estudiar(tipo,tamagotchi)
            tamagotchi.limpiar_interfaz()
            print("\n")
            print("regresando...")
            print("\n")
            time.sleep(2)
            tamagotchi.limpiar_interfaz()
        elif opcion == "5":
            tamagotchi.limpiar_interfaz()
            if tipo == "1":
                tamagotchi.dibujar_perro_mimir()
            elif tipo == "2":
                tamagotchi.dibujar_gato_mimir()
            elif tipo == "3":
                tamagotchi.dibujar_raton_mimir()
            tamagotchi.dormir(tipo,tamagotchi)
            tamagotchi.limpiar_interfaz()
            print("\n")
            print("regresando...")
            print("\n")
            time.sleep(2)
            tamagotchi.limpiar_interfaz()
        elif opcion == "6":
            tamagotchi.limpiar_interfaz()
            tamagotchi.sanar()
            time.sleep(2)
            tamagotchi.limpiar_interfaz()
            print("\n")
            print("regresando...")
            print("\n")
            time.sleep(2)
            tamagotchi.limpiar_interfaz()
        elif opcion == "1001":
            tamagotchi.establecer_todo_al_maximo()
        elif opcion == "0":
            tamagotchi.dejarjuego()
            tamagotchi.limpiar_interfaz()
            print("Has salido del juego.")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

        time.sleep(3)

        print("|-------------------------------------------------|")
        print('')
        if tipo == "1":
            tamagotchi.dibujar_perro()
        elif tipo == "2":
            tamagotchi.dibujar_gato()
        elif tipo == "3":
            tamagotchi.dibujar_raton()
        else:
            print(" ")
        print('')
        print("|-------------------------------------------------|")
        ############################################## Lo de abajo arreglar junto con la interfaz de los estado
        print('')
        tamagotchi.mostrar_estados()
        tamagotchi.mostrar_estados_maximos()
        time.sleep(1)
##########################
def main():
    tamagotchi = Tamagotchi("")
    tipo, nombre = nombre_tipo(tamagotchi)
    print("\n creando mascota")
    time.sleep(3)
    tamagotchi.limpiar_interfaz()

    print("|-------------------------------------------------|")
    print('')
    if tipo == "1":
        tamagotchi.dibujar_perro()
    elif tipo == "2":
        tamagotchi.dibujar_gato()
    elif tipo == "3":
        tamagotchi.dibujar_raton()
    else:
        print(" ")
    print('')
    print("|-------------------------------------------------|")

    tamagotchi.mostrar_estados()
    tamagotchi.mostrar_estados_maximos()

    acciones(tamagotchi, tipo)
#########################
def MenuInicial():
    print('')
    print('Bienvenido!')
    menu = False
    while menu == False:
        print('Elija una opcion: 1-Jugar  2-Instrucciones  3-Salir.')
        opcion = input()
        if opcion == '1':
            main()
            acciones()
        elif opcion == '2':
            Instrucciones()
        elif opcion =='3':
            DejarJuego()
            menu = True
        
        else: print('Ingrese una opcion disponible.')

###########################
MenuInicial()