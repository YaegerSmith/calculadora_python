#Mensaje de bienvenida.
print("¡Bienvenido a la calculadora!")
print("Calculadora que suma, resta, multiplica y divide.")
print()
#Menu de opciones
print("Eliga una de las opciones.")
print("1.- Suma.")
print("2.- Resta.")
print("3.- Multiplicación.")
print("4.- División.")
print("5.- Salir.")
opciones = int(input("Ingrese el número: "))
#Calcular la suma.
if opciones == 1:
    print("Eligio sumar.")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("La suma es igual a:", num1 + num2)
    print()
    print("Fin del programa.")
    print()
    exit()
#Calcular la resta. 
elif opciones == 2:
    print("Eligio restar")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print(num1 - num2)
    print()
    print("Fin del programa.")
    print()
    exit()
#Calcular la multiplicación.
elif opciones == 3:
    print("Eligio multiplicar.")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print(num1 * num2)
    print()
    print("Fin del programa.")
    print()
    exit()
#Calcular la división.
elif opciones == 4:
    print("Eligio dividir.")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print(num1 / num2)
    print()
    print("Fin del programa.")
    print()
    exit()
#Mensaje de salida.
elif opciones == 5:
    print("Fin del programa, regrese pronto.")
    print()
    exit()


