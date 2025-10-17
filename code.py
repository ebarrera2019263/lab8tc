import time
import matplotlib.pyplot as plt

def function_problem3(n):
    for i in range(1, n // 3 + 1):
        j = 1
        while j <= n:
            # Simulamos printf (no imprimimos para no saturar)
            _ = "Sequence"
            j += 4

# Valores de n según el enunciado
n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
times = []

print("n\t\tTiempo de ejecución (segundos)")
print("-" * 45)

for n in n_values:
    start = time.perf_counter()
    function_problem3(n)
    end = time.perf_counter()
    elapsed = end - start
    times.append(elapsed)
    print(f"{n}\t\t{elapsed:.8f}")

# Gráfica (guardada en la carpeta actual)
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, marker='o', linestyle='-', color='purple')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Tamaño de entrada (n) - escala logarítmica')
plt.ylabel('Tiempo de ejecución (s) - escala logarítmica')
plt.title('Problema 3: Tiempo de ejecución vs n')
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.savefig('plot.png')  # ← Guarda en la carpeta actual
plt.tight_layout()
plt.show()