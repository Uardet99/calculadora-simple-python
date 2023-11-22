print("¿Qué operación desea realizar?")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingrese el número de la operación deseada: ")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def switch(opcion):
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == "1":
        print("Resultado de la suma:", suma(num1, num2))
    elif opcion == "2":
        print("Resultado de la resta:", resta(num1, num2))
    elif opcion == "3":
        print("Resultado de la multiplicación:", multiplicacion(num1, num2))
    elif opcion == "4":
        print("Resultado de la división:", division(num1, num2))
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

# Llamamos a la función switch con la opción ingresada por el usuario
switch(opcion)

