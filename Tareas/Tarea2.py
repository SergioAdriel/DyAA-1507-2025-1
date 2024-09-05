def se_puede_formar(n):
    # Inicializar una lista booleana para almacenar si se puede formar cada número de plumas
    dp = [False] * (n + 1)
    dp[0] = True  # Es posible formar 0 plumas (no comprar ningún paquete)

    # Paquetes disponibles
    paquetes = [5, 8, 24]

    # Llenar la lista dp
    for i in range(1, n + 1):
        for paquete in paquetes:
            if i >= paquete and dp[i - paquete]:
                dp[i] = True
                break

    return dp[n]

# Ejemplo de uso
n = int(input("Ingrese el número de plumas: "))
if se_puede_formar(n):
    print(f"Es posible formar {n} plumas con los paquetes disponibles.")
else:
    print(f"No es posible formar {n} plumas sin abrir un paquete.")
