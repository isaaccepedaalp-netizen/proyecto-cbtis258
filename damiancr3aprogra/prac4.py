suma_notas = 0
notas = []

for i in range(5):
    nota = float(input("Insertar calificacion: "))
    notas.append(nota)
    suma_notas += nota

print("Notas guardadas:", notas)
print("Suma de las notas:", suma_notas)