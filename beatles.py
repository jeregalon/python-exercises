beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)

for i in range(2):
    beatles.append(input("Agrega otro artista a la banda: "))
print(beatles)

for i in range(2):
    del beatles[len(beatles) - 1]
print(beatles)

beatles.insert(0, "Ringo Starr")
print(beatles)



