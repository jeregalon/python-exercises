# TODO: Agregar letras a la lista de segments 

import time, os

segments = [
    """###
# #
# #
# #
###""",
    """#
#
#
#
#""",
    """###
  #
###
#  
###""",
     """###
  #
###
  #
###""",
     """# #
# #
###
  #
  #""",
    """###
#  
###
  #
###""",
    """###
#  
###
# #
###""",
    """###
  #
  #
  #
  #""",
    """###
# #
###
# #
###""",
    """###
# #
###
  #
###""" 
]

def cleanConsole():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

fixedText = ""
numSequence = ""
numOfSpaces = -1

while numSequence == "":
    numSequence = input("Introduzca una secuencia de números enteros: ")
    if numSequence.isdecimal():
        segLines = [segments[int(num)].splitlines() for num in numSequence]
    else:
        print("Por favor, introduzca solo números")
        numSequence = ""

while numOfSpaces < 0:
    try:
        numOfSpaces = int(input("Introduzca la cantidad de espacios: "))
        if not (0 <= numOfSpaces <= 10):
            print("La cantidad de espacios debe ser de 0 a 10")
            numOfSpaces = -1
        else:
            pass
    except:
        print("Debe introducir un número del 0 al 10")

    
for i in range(5):
    for line in segLines:
        fixedText += ' ' * numOfSpaces + line[i]
    fixedText += "\n"

while True:
    time.sleep(0.1)
    textLines = fixedText.splitlines()
    fixedText = ""
    for i in range(5):
        textLines[i] = textLines[i][1:] + textLines[i][0]
        fixedText += textLines[i] + "\n"
    cleanConsole()
    print(fixedText)
  

