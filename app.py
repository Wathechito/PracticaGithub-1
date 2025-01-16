# desafio: calcular la edad de una persona
# primer desafio consiste en no usar input()
# rama main

año_actual = 2025
año_nacimiento = 1994
condicion = True # True si la persona ya cumplio años, False si no los ha cumplido

edad = año_actual - año_nacimiento

if condicion == False:
    print(f"La edad de la persona es: {edad} años")
else:
    print(f"La edad de la persona es: {edad - 1} años")