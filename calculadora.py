print("================================")
print("       CALCULADORA BÁSICA")
print("================================")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\nSeleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingrese el número de la operación: ")

if opcion == "1":
    print("Resultado:", num1 + num2)

elif opcion == "2":
    print("Resultado:", num1 - num2)

elif opcion == "3":
    print("Resultado:", num1 * num2)

elif opcion == "4":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: No se puede dividir entre cero.")

else:
    print("Opción no válida.")
