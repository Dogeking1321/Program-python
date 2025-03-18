cal = 0
while True:
    num = int(input("Podaj liczbę całkowitą: "))
    if num % 13 == 0:
        break
    if num >= 0:
        cal += num  

print(f"Suma zgromadzonych liczb nieujemnych: {cal}")

