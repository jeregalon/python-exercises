# TODO:
# Adaptar el programa al alfabeto español (que el usuario pueda escoger entre español e inglés)
# Hacer que descifre una secuencia comparando las palabras del mensaje con las de un diccionario 

message = input("Escribe un mensaje que quieras cifrar: ")
ciphMessage = ""
shift = 0

while True:
    try:    
        shift = int(input("Introduzca un número del 1 al 25: "))
        while not (1 <= shift <= 25):
            shift = int(input("Debe ser un número del 1 al 25: "))
        break
    except:
        print("Debe introducir un valor numérico")

for letter in message:
    nextChar = ""
    pos = ord(letter)

    if letter.isalpha():
        lastPos = 122 if 97 <= pos <= 122 else 90   # si la letra es minúscula, lastPos es la posición del caracter "z"
                                                    # si es mayúscula, lastPos es la posición del caracter "Z"
        if pos + shift <= lastPos:
            nextChar = chr(pos + shift)
        else:
            nextChar = chr(pos + shift - 26)
    else:
        nextChar = letter

    ciphMessage += nextChar

print(ciphMessage)