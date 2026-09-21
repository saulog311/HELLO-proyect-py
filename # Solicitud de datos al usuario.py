# Solicitud de datos al usuario
Peso= float(input("Ingresa tu peso en kilogramos"))
Altura= float(input("Ingrasa tu altura en metros"))

# Cálculo del IMC(Peso/Altura^2)
IMC= Peso/Altura**2

# Mostrar el resultado al usuario
print("Tu Índice de Masa Corporal (IMC) es:", IMC)

if IMC < 18.5:
    clasificacion = "Bajo peso"
elif IMC < 24.9:
    clasificacion = "Peso normal"
elif IMC <= 29.9:
    clasificacion = "Sobrepeso"
else: 
    clasificacion = "Obesidad"

# Mostrar de resultado
print("Tu Índice de Masa Corporal (IMC) es:", IMC)
print(f"Tu clasificación es: {clasificacion}")