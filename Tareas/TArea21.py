import matplotlib.pyplot as plt
import numpy as np

# Valores de n
n = np.linspace(1, 100, 400)

# Definición de las funciones de complejidad
O_1 = np.ones_like(n)
O_n = n
O_log_n = np.log(n)
O_n_log_n = n * np.log(n)
O_n2 = n**2

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(n, O_1, label='O(1)')
plt.plot(n, O_n, label='O(n)')
plt.plot(n, O_log_n, label='O(log n)')
plt.plot(n, O_n_log_n, label='O(n log n)')
plt.plot(n, O_n2, label='O(n^2)')

# Configuración de la gráfica
plt.ylim(0, 1000)
plt.xlabel('n')
plt.ylabel('Tiempo de ejecución')
plt.title('Gráficas de Complejidad')
plt.legend()
plt.grid(True)
plt.show()
