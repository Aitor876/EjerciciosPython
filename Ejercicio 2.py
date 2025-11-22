def doble_factorial(n):
    if n < 0:
        raise ValueError("El número no debe ser negativo.")
    
    if n == 0 or n == 1:
        return 1
    
    return n * doble_factorial(n - 2)


try:
    numero = int(input("Escribe un número entero: "))
    resultado = doble_factorial(numero)
    print(f"El doble factorial de {numero} es {resultado}")
except ValueError as e:
    print(f"Error: {e}")
