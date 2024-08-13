#PROYECTO FINAL

print ("-"*10 + "CHATBOT" + "-"*10 )
print ("Pista: Comienza diciendo <hola>.")

import random 

diccionario = {
    "hola": ("Hola. ¿Cómo estás?", "¡Saludos! ¿Hay algo en lo que pueda ayudarte?"), 
    "cómo estás": ("Estoy bien.", "Yo bien, gracias por preguntar."),
    "adiós": (),
    "qué te gusta hacer": ("Me gusta aprender cosas nuevas y conversar con gente interesante.", "Disfruto mucho ayudando a otros."),
    "qué puedes hacer": ("Puedo responder a tus preguntas y ayudarte con información.", "Puedo conversar contigo sobre varios temas."),
    "tarea": (),
    "mascota": ("Como soy un modelo de lenguaje, no tengo mascotas. Pero me encantaría tener un perro algún día.", "Las mascotas son un poco raras para mí."),
    "comida": ("No puedo comer, pero si pudiera, me gustaría probar la cocina de todas las culturas del mundo.", "No, no tengo. Soy un robot."),
    "nombre": (),
    "chiste": (),
    "ayuda": ()
}

nombre= ["Tu nombre es muy extraño.", 
         "¡Es un nombre muy bonito!", 
         "No me gusta tu nombre. Deberías llamarte Juanito Alcachofa.",
         "¡Qué nombre tan único! Me gusta.",
         "Tu nombre tiene un sonido muy agradable.",
         "Es un placer conocerte, aunque no pueda pronunciar tu nombre a la perfección."]

response= ["¡Pregúntame algo!", "¿Hay algo en lo que pueda ayudarte?", "¿Necesitas ayuda en algo?", 
           "Estoy aquí para ayudarte, ¿en qué puedo ser útil?", "Si tienes preguntas, soy todo oídos."]

despedida= ["Adiós. ¡Feliz resto del día!", 
            "Bye. Ojalá hablar contigo otra vez.", 
            "Nos vemos pronto, ¡cuídate!",
            "¡Hasta la próxima, que tengas un buen día!", 
            "Despedirme de ti es como apagar mi energía... ¡Nos vemos pronto!"]

chistes= ["a: ¿Cómo se llama el campeón de buceo japonés?. b:Tokofondo. a: ¿Y el subcampeón?. b: Kasitoko", 
          "Si car es carro y men es hombre entonces Carmen es un transformer...",
           "Prepárate para reír, aquí va uno: ¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
            "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter." ]

chistes_negros= ["¿Porqué los negros son zurdos? Porque no tienen derechos", 
                 "a: ¿Por qué no tiran bombas a África? b: Porque no encuentran el blanco",
                 "¿Por qué no juegan al escondite en África? Porque el que se esconde bien nunca lo encuentran."]



def matemáticas():
    while True:
        try: 
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            op = input("Ingrese la operación a realizar (+, -, *, /, **): ")
            
            if op == "+":
                resultado = num1 + num2       
            elif op == "-":
                resultado = num1 - num2
            elif op == "*":
                resultado = num1 * num2
            elif op == "/":
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("No se puede dividir entre 0.")
                    chatboteando_mates()
            elif op == "**":
                resultado = num1 ** num2
            else:
                print("Operación no válida.")
                continue 

            print(f"El resultado es: {resultado}")
        except ValueError:
            print("Por favor, ingrese números válidos.")
        except Exception as i:
            print ("Ocurrió un error inesperado.")

        continuar = (input("¿Desea continuar? (si/no): ")).lower()

        if continuar == "no":
            chatboteando()
        else:
            continue

def chatboteando_mates():
    entrada = input("¿Necesitas ayuda en matemáticas? (si/no): ").lower()
    if entrada == "si":
        matemáticas()
    else: 
        chatboteando()

def nombrando():
    try:
        print("No tengo nombre, pero... ¿Podrías decirme el tuyo?")
        entrada = input("Tú: ")
        print(f"{entrada}... " + random.choice(nombre))
    except Exception as i:
        print("Ocurrió un error inesperado al procesar el nombre.")

def start_chistecito():

    x=0
    while x<1:
        print("¿Te gustaría leer un chiste? (si/no)")
        entrada= input("Tú:" ).lower()
        if entrada== "no": 
            x+= 1
            chatboteando()
        if entrada== "si": 
            x+= 1
            chistecito()
            return
        else:
            print ("Respuesta inválida")


def chistecito():
    contador= 0
    while True: 
        contador+= 1
        if contador <= 4:
            print(random.choice(chistes))
        else: 
            print(random.choice(chistes_negros))

        print ("¿Quieres escuchar otro chiste? (si/no)")

        entrada= (input("Tú: ")).lower()
        if entrada== "no":
             chatboteando()
        else: 
            continue

        

def despidiendo():
    print(random.choice(despedida))
    exit()

def chatboteando():
    print(random.choice(response))
    while True:
        entrada = input("Tú: ").lower()
        respuesta = None  
        
        try: 
            for clave in diccionario:
                if clave in entrada:
                    if clave == "tarea":
                        chatboteando_mates()
                    elif clave == "nombre":
                        nombrando()
                    elif clave == "adiós":
                        despidiendo()
                    elif clave== "chiste":
                        start_chistecito()
                        return
                    
                    respuesta = random.choice(diccionario[clave])
                    break   
                
            if respuesta:
                print(f"{respuesta}")
            else:
                print("Lo siento, no entendí eso. ¿Podrías repetirlo o reformularlo?")
        except Exception as i:
            None

chatboteando()
