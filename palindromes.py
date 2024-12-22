text = ""
testText = ""

def reverseText(txt):
    reversedTxt = ""
    for i in range(len(txt)):
        reversedTxt += txt[len(txt) - 1 - i]
    return reversedTxt

while True:
    text = input("Escriba una cadena de texto: ")
    while len(text) == 0:
         text = input("Escribe algo, porfa: ")
    break

for ch in text:
    if ch.isalpha():
        testText += ch.lower()
    else:
        pass

if testText == reverseText(testText):
    print("Tu texto es un palíndromo \o/")
else:
    print("No es un palíndromo :p")