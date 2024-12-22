def cifrado_cesar():
    language = input("\nEscoge un lenguaje (español: e, inglés: i): ").strip().lower()
    while language not in ("e", "i"):
        language = input("Debes escoger 'e' o 'i': ").strip().lower()

    is_spanish = language == "e"
    max_shift = 27 if is_spanish else 26

    while True:
        try:
            shift = int(input(f"Introduce un número entre 1 y {max_shift}: "))
            if 1 <= shift <= max_shift:
                break
        except ValueError:
            pass
        print(f"Debe ser un número válido entre 1 y {max_shift}.")

    mensaje = input("\nEscribe un mensaje a cifrar: ")
    if is_spanish:
        mensaje = mensaje.translate(str.maketrans("áéíóú", "aeiou"))

    def cifrar_caracter(c):
        if c.isalpha():
            abecedario = "abcdefghijklmnñopqrstuvwxyz" if is_spanish else "abcdefghijklmnopqrstuvwxyz"
            abecedario = abecedario.upper() if c.isupper() else abecedario
            nueva_pos = (abecedario.index(c) + shift) % len(abecedario)
            return abecedario[nueva_pos]
        return c

    mensaje_cifrado = "".join(cifrar_caracter(c) for c in mensaje)
    print("\nMensaje cifrado:", mensaje_cifrado)

cifrado_cesar()
