import math as mt

def area_figuras():
    print("Calculadora de Áreas y Perímetros")
    print("Seleccione la figura para calcular:")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")
    
    opcion = input("Ingrese el número de la figura (1-4): ")
    
    if opcion == '1':
        lado = float(input("Ingrese la longitud del lado del cuadrado: "))
        area = lado ** 2
        perimetro = 4 * lado
        print(f"Área del cuadrado: {area}")
        print(f"Perímetro del cuadrado: {perimetro}")
        return area
        
    elif opcion == '2':
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = base * altura
        perimetro = 2 * (base + altura)
        print(f"Área del rectángulo: {area}")
        print(f"Perímetro del rectángulo: {perimetro}")
        return area
        
    elif opcion == '3':
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
        lado_1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
        lado_2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
        lado_3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))
        perimetro = lado_1 + lado_2 + lado_3
        print(f"Área del triángulo: {area}")
        print(f"Perímetro del triángulo: {perimetro}")
        return area
        
    elif opcion == '4':
        radio = float(input("Ingrese el radio del círculo: "))
        area = mt.pi * (radio ** 2)
        perimetro = 2 * mt.pi * radio
        print(f"Área del círculo: {area}")
        print(f"Perímetro del círculo: {perimetro}")
        return area
        
    else:
        print("Opción no válida. Por favor, seleccione una figura válida.")

def perimetro_figuras():
    print("Calculadora de Perímetros")
    print("Seleccione la figura para calcular:")
    print("1. Cuadrado", "2. Rectángulo", "3. Triángulo", "4. Círculo")
    
    opcion = input("Ingrese el número de la figura (1-4): ")
    
    if opcion == '1':
        lado = float(input("Ingrese la longitud del lado del cuadrado: "))
        perimetro = 4 * lado
        print(f"Perímetro del cuadrado: {perimetro}")
        return perimetro
        
    elif opcion == '2':
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        perimetro = 2 * (base + altura)
        print(f"Perímetro del rectángulo: {perimetro}")
        return perimetro
        
    elif opcion == '3':
        lado_1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
        lado_2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
        lado_3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))
        perimetro = lado_1 + lado_2 + lado_3
        print(f"Perímetro del triángulo: {perimetro}")
        return perimetro

    elif opcion == '4':
        radio = float(input("Ingrese el radio del círculo: "))
        perimetro = 2 * mt.pi * radio
        print(f"Perímetro del círculo: {perimetro}")
        return perimetro
        
    else:
        print("Opción no válida. Por favor, seleccione una figura válida.")


print('\"Bienvenido a la Calculadora de Áreas y Perímetros\"' )
print("Seleccione la opción que desea calcular:")
print("1. Áreas", "2. Perímetros")
opcion = input("Ingrese el número de la opción (A-P): ")

if opcion == 'A':
    print(area_figuras())
elif opcion == 'P':
    print(perimetro_figuras())
else:
    print("Opción no válida. Por favor, seleccione una opción válida.")