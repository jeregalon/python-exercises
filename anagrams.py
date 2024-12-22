frase1 = ""
frase2 = ""
sonAnag = False

while True:
    frase1 = input("Digita una frase: ")
    while not "".join(frase1.split(" ")).isalpha():
        frase1 = input("La frase solo debe contener letras y espacios. Intenta de nuevo: ")
    break

while True:
    frase2 = input("Digita otra frase: ")
    while not "".join(frase2.split(" ")).isalpha():
        frase2 = input("La frase solo debe contener letras y espacios. Intenta de nuevo: ")
    break

if len(frase1) - frase1.count(" ") == len(frase2) - frase2.count(" "):
    for ch in frase1:
        if frase1.count(ch) != frase2.count(ch):
            break
        sonAnag = True

print("¡Las frases son anagramas!" if sonAnag else "No son anagramas :P") 
