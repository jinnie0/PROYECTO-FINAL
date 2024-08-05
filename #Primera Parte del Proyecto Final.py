#PROYECTO FINAL 


import random 

diccionario = {
    "hola": ("Hola. ¿Cómo estás?", "¡Saludos! ¿Hay algo en lo que pueda ayudarte?"), 
    "cómo estás": ("Estoy bien. ¿Y tú?", "Yo bien, gracias por preguntar. ¿Tú cómo estás?"),
    "adiós": ("Adiós. ¡Feliz resto del día!", "Bye. Ojalá hablar contigo otra vez."),
    "qué te gusta hacer": ("Me gusta aprender cosas nuevas y conversar con gente interesante.", "Disfruto mucho ayudando a otros."),
    "qué puedes hacer": ("Puedo responder a tus preguntas y ayudarte con información.", "Puedo conversar contigo sobre varios temas."),
    "tarea": ()}


def matemáticas():
    continuar=0
    resultado=0
    while continuar==0:
        num1= input("Ingrese el primer numero: ")
        num2= input("Ingrese el segundo numero: ")
        
        op= input("Ingrese la operacion a realizar: ")
        if op == "+":
            resultado= float(num1) + float(num2)
            print(resultado)
            
        elif op == "-":
            resultado= float(num1) - float(num2)

        elif op == "*":
            resultado= float(num1) * float(num2)
            print(resultado)
        elif op == "/":
            resultado= float(num1) / float(num2)
            print(resultado)
        elif op == "**":
            resultado= float(num1) ** float(num2)
            print(resultado)
        else:
            print("Operacion no valida")

        continuar= int(input("¿Desea continuar? 0=Si, 1=No: "))

        if continuar== 1:
            chatboteando()




def chatboteando_mates ():
    entrada= input("¿Necesitas ayuda en matemáticas? (si/no): ")
    if entrada == "si":
        matemáticas()
        return
    else: 
        chatboteando()
        return
        

def chatboteando():
    print("¿En qué puedo ayudarte? ¡Charla conmigo!")
    while True:
        
        entrada= input("Tú: ")
        entrada = entrada.lower()

        for clave in diccionario:
            if clave in entrada:
                if clave=="tarea":
                  chatboteando_mates()
                  return
            
                respuesta = random.choice(diccionario[clave])
                break   
        if respuesta:
            print(f"{respuesta}")
        else:
            print("Lo siento, no entendí eso. ¿Podrías repetirlo o reformularlo?")

chatboteando()




