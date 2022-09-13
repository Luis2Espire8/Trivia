BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
puntaje = [0] 

def preguntas():
    print (GREEN+"Bueno veo que vienes con animo,Empezemos con tu nombre"+RESET)
    nombre = input(BLUE +"Escribe tu nombre:"+RESET)
    nombre = nombre.capitalize()
    mdp = f"""
     {BLUE} Comenzamos con las preguntas Recuerda que todas tus respuestas seran evaluadas 📚💯{RESET}
""" 
    print(mdp)
    pregunta1 = f"""{GREEN}bien {nombre} ,¿Quien escribio el señor de los anillos?:{RESET} {YELLOW}
    a) George Raymond Richard Martin
    b) Frank Herbert
    c) Herbert George Wells
    d) John Ronald Reuel Tolkien
    {RESET}
    """
    print(pregunta1)
    respuesta_1 = input(BLUE+"Escribe tu respuesta: "+RESET)
    respuesta_1 = respuesta_1.lower()
    while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input(BLUE+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
        respuesta_1 = respuesta_1.lower()
    if respuesta_1 == "a":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+"Incorrecto! ",nombre,' ,George Raymond Richard Martin es reconocido por su obra literaria "Juego de Tronos"'," tienes ",puntajenuevo ," puntos"+RESET)
        
    elif respuesta_1 == "b":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+"Incorrecto! ",nombre,' ,Frank Herbert es reconocido por su obra literaria "Dune"'," tienes ",puntajenuevo ," puntos"+RESET)

    elif respuesta_1 == "c":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+"Incorrecto! ",nombre,',Frank Herbert es reconocido por su obra literaria "La Guerra de los Mundos"'," tienes ",puntajenuevo ," puntos"+RESET)

    else:
        puntaje.append (20)
        puntajenuevo=sum(puntaje)
        print (CYAN+"Muy bien", nombre, "!"," ,tienes ",puntajenuevo ," puntos"+RESET)
    
    pregunta2 = f"""{GREEN}¿Donde nacio el escritor Gabriel Garcia Marquez?{RESET}{YELLOW}
    a) Bolivia
    b) Colombia 
    c) Venezuela
    d) Ecuador {RESET}
    """
    print(pregunta2)
    respuesta_2 = input(BLUE+"Escribe tu respuesta: "+RESET)
    respuesta_2 = respuesta_2.lower()
    while respuesta_2 not in ("a", "b", "c", "d"):
        respuesta_2 = input(BLUE+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
        respuesta_2 = respuesta_2.lower()
    if respuesta_2 == "a":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+"Incorrecto! ",nombre," tienes ",puntajenuevo ," puntos"+RESET)
        
    elif respuesta_2 == "c":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+"Incorrecto! ",nombre," tienes ",puntajenuevo ," puntos"+RESET)

    elif respuesta_2 == "d":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+"Incorrecto! ",nombre," tienes ",puntajenuevo ," puntos"+RESET)

    else:
        puntaje.append (20)
        puntajenuevo=sum(puntaje)
        print (CYAN+"Muy bien el es de Colombia", nombre, "!"," tienes ",puntajenuevo ," puntos"+RESET)

    pregunta3 = f"""{GREEN}¿Cual era el sobrenombre de William shakespeare?{RESET}{YELLOW}
    a) El cisne de avon
    b) El cisne plateado
    c) La Pluma triste
    d) El enamorado {RESET}
    """
    print(pregunta3)
    respuesta_3 = input(BLUE+"Escribe tu respuesta: "+RESET)
    respuesta_3 = respuesta_3.lower()
    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input(BLUE+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
        respuesta_3 = respuesta_3.lower()
    if respuesta_3 == "b":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+"Incorrecto! ",nombre," tienes ",puntajenuevo ," puntos"+RESET)
        
    elif respuesta_3 == "c":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+"Incorrecto! ",nombre," tienes ",puntajenuevo ," puntos"+RESET)

    elif respuesta_3 == "d":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+"Incorrecto! ",nombre," tienes ",puntajenuevo ," puntos"+RESET)

    else:
        puntaje.append (20)
        puntajenuevo=sum(puntaje)
        print (CYAN+"Asi Conocian a William Shakespeare porque decian que el no pertenecia a una determinada época, sino a la eternidad!"," tienes ",puntajenuevo ," puntos"+RESET)

    pregunta4 = f"""{GREEN}¿Quien fue el escritor de la Divina Comedia?{RESET}{YELLOW}
    a) Dante Alighieri
    b) Homero
    c) Madeline Miller
    d) Virgilio {RESET}
    """
    print(pregunta4)
    respuesta_4 = input("Escribe tu respuesta: ")
    respuesta_4 = respuesta_4.lower()
    while respuesta_4 not in ("a", "b", "c", "d"):
        respuesta_4 = input(BLUE+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
        respuesta_4 = respuesta_4.lower()
    if respuesta_4 == "b":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+'Incorrecto! Homero fue Conocido por escribir la "Odisea",',nombre," tienes ",puntajenuevo ," puntos"+RESET)
        
    elif respuesta_4 == "c":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+'Incorrecto! Madeline Miller es conocida por "La canción de aquiles",',nombre," tienes ",puntajenuevo ," puntos"+RESET)

    elif respuesta_4 == "d":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+'Incorrecto! VIrgilio fue conocido por "Eneida",',nombre," tienes ",puntajenuevo ," puntos"+RESET)

    else:
        puntaje.append (20)
        puntajenuevo=sum(puntaje)
        print (CYAN+'Dante Alighieri escribio una de las obras fundamentales de la transición del pensamiento medieval al renacentista y una de las cumbres de la literatura universal."La Divina Comedia" '," tienes ",puntajenuevo ," puntos"+RESET)
        
    pregunta5 = f"""{GREEN}¿En que año  el escritor Mario Vargas Lloza gano su premio nobel?{RESET} {YELLOW}
    a) 2009
    b) 2008
    c) 2010
    d) 2001 {RESET}
    """
    print(pregunta5)
    respuesta_5 = input("Escribe tu respuesta: ")
    respuesta_5 = respuesta_5.lower()
    while respuesta_5 not in ("a", "b", "c", "d"):
        respuesta_5 = input(BLUE+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
        respuesta_5 = respuesta_5.lower()
    if respuesta_5 == "a":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+"Incorrecto! fue en el año 2010 ",nombre," tienes ",puntajenuevo ," puntos"+RESET)
        
    elif respuesta_5 == "b":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+"Incorrecto! fue en el año 2010",nombre," tienes ",puntajenuevo ," puntos"+RESET)

    elif respuesta_5 == "d":
        puntaje.append (-10)
        puntajenuevo=sum(puntaje)
        print (RED+"Incorrecto! fue en el año 2010",nombre," tienes ",puntajenuevo ," puntos"+RESET)

    else:
        puntaje.append (20)
        puntajenuevo=sum(puntaje)
        print (CYAN+"El escritor y político peruano Mario Vargas Llosa fue galardonado con el Premio Nobel de Literatura en el año 2010 por su trayectoria literaria!"," tienes ",puntajenuevo ," puntos"+RESET)
        
    final = f"""
    {BLUE}{nombre} Este es el final de la trivia, Muchas gracias por participar ♥
                TU PUNTAJE ES : {puntajenuevo}{RESET}"""
    print(final)
    
    

menu = f"""{BLUE}
            📚📚 Bienvenido a mi trivia de Literatura 📚📚
           Pondremos a prueba tu conocimiento en esta trivia
            Esta Trivia consta de 5 preguntas con puntaje
            {RESET}
           
"""

print(menu)

listo = input(BLUE+"¿Estas preparado?: "+RESET)
listo = listo.lower()
if listo == "si":    
    preguntas()

else:
    print("Vuelve cuando estes listo")