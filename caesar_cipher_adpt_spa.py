language = ""

while True:
    language = input("\nEscoge un lenguaje para tu mensaje:\nespañol(e)\ninglés(i): ")
    while not (language.startswith("e") or language.startswith("i")):
        language = input("\nDebes escoger entre:\nespañol(e)\ninglés(i): ")
    break

isMessageInSpanish = True if language.startswith("e") else False

message = input("\nEscribe un mensaje que quieras cifrar: ")

if isMessageInSpanish:          # las letras con tilde se cambian por letras sin tilde
    message = message.replace("á", "a") \
    .replace("é", "e") \
    .replace("í", "i") \
    .replace("ó", "o") \
    .replace("ú", "u")

ciphMessage = ""
shift = 0
maxShift = 26 if isMessageInSpanish else 25

while True:
    try:    
        shift = int(input(f"\nIntroduzca un número del 1 al {maxShift}: "))
        while not (1 <= shift <= maxShift):
            shift = int(input(f"\nDebe ser un número del 1 al {maxShift}: "))
        break
    except BaseException as err:
        print("Debe introducir un valor numérico")

for letter in message:
    nextChar = ""
    pos = ord(letter)

    if letter.isalpha():
        firstPos = 97 if 97 <= pos <= 122 or pos == 241 else 65     # posición de la a o A

        lastPos = 122 if 97 <= pos <= 122 or pos == 241 else 90     # si la letra es minúscula, lastPos es la posición del caracter "z"
                                                                    # si es mayúscula, lastPos es la posición del caracter "Z"
        jump = 110 if 97 <= pos <= 122 or pos == 241 else 78        # posición de la n o N. Si el mensaje está escrito en español, habrá un salto
                                                                    # para incluir la letra ñ o Ñ
        posnn =  241 if 97 <= pos <= 122 or pos == 241 else 209     # posición de la ñ o Ñ

        if (isMessageInSpanish and ((pos < jump + 1 and pos + shift <= lastPos + 1) or (pos == posnn and shift < 13))) or pos + shift <= lastPos:
            if isMessageInSpanish and (pos <= jump or pos == posnn):     # si el mensaje está en español, y el caracter es menor o igual que ñ o Ñ 
                if pos != posnn:
                    if pos + shift == jump + 1:     # si la posición del caracter más el shift es igual a la posición de la letra o u O
                        nextChar = chr(posnn)            # el próximo caracter será ñ o Ñ
                    elif pos + shift > jump + 1:    # si es mayor que o u O
                        nextChar = chr(pos + shift - 1)     # al próximo caracter se le resta 1 (para incluir la ñ o Ñ)
                    else:
                        nextChar = chr(pos + shift) # sino, el desplazamiento se mantiene normal
                else:               # si el caracter es la letra ñ o Ñ
                    pos = jump      # el caracter pasará a ser n o N
                    nextChar = chr(pos + shift)
            else:                               # si el caracter es o u O, o mayor, o el mensaje está en inglés
                nextChar = chr(pos + shift)
        else:                                   # si el caracter más el shift se pasa de la letra z o Z
            if (pos != posnn):
                if pos <= jump or not isMessageInSpanish:
                    nextChar = chr(pos + shift - (maxShift + 1))    # se le resta 26 a la posición más el desplazamiento (z + 1 sería a, z + 2 sería b, etc.)
                else:
                    nextChar = chr(pos + shift - maxShift)
                if isMessageInSpanish:              # si el mensaje está en español
                    if ord(nextChar) == jump + 1:        # y nextChar es igual a o u O:
                        nextChar = chr(posnn)       # nextChar pasa a ser ñ o Ñ
                    elif ord(nextChar) > jump + 1:       # si nextChar es mayor que o u P
                        nextChar = chr(ord(nextChar) - 1)   # se resta nextChar en 1 para incluir la ñ en el conteo
                    else:
                        pass                        # sino, se mantiene igual a que si el mensaje estuviera en inglés
            else:
                nextChar = chr(firstPos + shift - 13)
    else:
        nextChar = letter

    ciphMessage += nextChar

print(ciphMessage)