# desafio: calcular la edad de una persona
# primer desafio consiste en no usar input()
# rama main_2 act.

año_actual = int(input('Ingresa el año actual: '))
print("\n")

año_nacimiento = int(input('Ingrese tu año de nacimiento: '))
print("\n")

# True si la persona ya cumplio años, False si no los ha cumplido
años_cumplidos = input('¿Ya cumplistes años? (si/no): ')
print("\n")

if años_cumplidos == 'si':
    años_cumplidos = True
else:
    años_cumplidos = False

edad = año_actual - año_nacimiento

if años_cumplidos == True:
    print(f"Tu edad es: {edad} años")
else:
    print(f"Tu edad es: {edad - 1} años")