hat = [i + 1 for i in range(5)]
num = int(input("Escribe un número entero: "))
hat[2] = num
del hat[len(hat) - 1]
print(len(hat))