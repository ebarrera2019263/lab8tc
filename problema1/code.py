import time
import matplotlib.pyplot as plt
import numpy as np

def function_problem1(n):
    counter = 0
    start_i = n // 2
    max_j = n - (n // 2)  # porque j + n//2 <= n → j <= n - n//2
    for i in range(start_i, n + 1):
        for j in range(1, max_j + 1):
            k = 1
            while k <= n:
                counter += 1
                k *= 2
    return counter

def measure_time(n, runs=5):
    """Mide el tiempo promedio de ejecución en 'runs' corridas."""
    if n == 0:
        return 0.0
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        function_problem1(n)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)

# Valores de n requeridos por el enunciado
n_values_all = [1, 10, 100, 1000, 10000, 100000, 1000000]
n_values_measured = [1, 10, 100, 1000, 10000]  # hasta aquí medimos
n_values_estimated = [100000, 1000000]

# Medir tiempos reales
print("n\t\tTiempo de ejecución (segundos)")
print("-" * 50)
times_measured = {}
for n in n_values_measured:
    t = measure_time(n, runs=5)
    times_measured[n] = t
    print(f"{n}\t\t{t:.8f}")

# Estimar tiempos para n grandes usando T(n) = c * n^2 * log2(n)
# Usamos el último punto medido (n=10000) para calcular 'c'
n_ref = 10000
t_ref = times_measured[n_ref]
c = t_ref / (n_ref**2 * np.log2(n_ref))

times_estimated = {}
for n in n_values_estimated:
    t_est = c * (n**2) * np.log2(n)
    times_estimated[n] = t_est
    print(f"{n}\t\t{t_est:.8f} (estimado)")

# Combinar todos los tiempos
all_n = n_values_all
all_times = [times_measured.get(n, times_estimated.get(n)) for n in all_n]

# --- GRÁFICA ---
plt.figure(figsize=(10, 6))

# Puntos reales
real_n = [n for n in all_n if n in times_measured]
real_t = [times_measured[n] for n in real_n]
plt.plot(real_n, real_t, 'bo-', label='Medido', markersize=6)

# Puntos estimados
est_n = [n for n in all_n if n in times_estimated]
est_t = [times_estimated[n] for n in est_n]
plt.plot(est_n, est_t, 'r^--', label='Estimado', markersize=6)

# Línea de referencia O(n² log n)
n_ref_line = np.array(real_n + est_n)
t_ref_line = c * (n_ref_line**2) * np.log2(n_ref_line + 1)
plt.plot(n_ref_line, t_ref_line, 'g:', label='O(n² log n)', linewidth=1)

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Tamaño de entrada (n) - escala logarítmica')
plt.ylabel('Tiempo de ejecución (s) - escala logarítmica')
plt.title('Problema 1: Tiempo de ejecución vs n')
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend()
plt.savefig('problem1_plot.png')
plt.tight_layout()
plt.show()