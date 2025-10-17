# problem3.py
import time
import matplotlib.pyplot as plt
import numpy as np

def function_problem3(n):
    for i in range(1, n // 3 + 1):
        j = 1
        while j <= n:
            _ = "Sequence"  # Simulamos printf
            j += 4

def measure_time(n, runs=3):
    if n == 0:
        return 0.0
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        function_problem3(n)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)

# Valores requeridos por el enunciado
n_values_all = [1, 10, 100, 1000, 10000, 100000, 1000000]
n_measured = [1, 10, 100, 1000, 10000, 100000]  # omitimos 1e6 por tiempo
n_estimated = [1000000]

print("n\t\tTiempo de ejecución (segundos)")
print("-" * 50)

times_dict = {}

# Medir tiempos reales
for n in n_measured:
    t = measure_time(n, runs=3)
    times_dict[n] = t
    print(f"{n}\t\t{t:.8f}")

# Estimar n = 1e6 usando T(n) = c * n^2
n_ref = 100000
t_ref = times_dict[n_ref]
c = t_ref / (n_ref ** 2)

t_est = c * (1000000 ** 2)
times_dict[1000000] = t_est
print(f"1000000\t\t{t_est:.8f} (estimado)")

# Preparar datos para gráfica
all_n = n_values_all
all_t = [times_dict[n] for n in all_n]

n_real = [n for n in all_n if n <= 100000]
t_real = [times_dict[n] for n in n_real]

n_est = [1000000]
t_est_list = [times_dict[1000000]]

# --- GRÁFICA ---
plt.figure(figsize=(10, 6))
plt.plot(n_real, t_real, 'bo-', label='Medido', markersize=7)
plt.plot(n_est, t_est_list, 'r^--', label='Estimado', markersize=7)

# Línea de referencia O(n²)
n_smooth = np.logspace(0, 6, 100)
t_ref_line = c * (n_smooth ** 2)
plt.plot(n_smooth, t_ref_line, 'g:', label='O(n²)', linewidth=1.5)

plt.xscale('log')
plt.yscale('log')
plt.xlabel('n (escala logarítmica)')
plt.ylabel('Tiempo de ejecución (s, escala logarítmica)')
plt.title('Problema 3: Tiempo vs n (con estimación)')
plt.grid(True, which="both", ls="--", alpha=0.7)
plt.legend()
plt.savefig('problem3_plot.png', dpi=150, bbox_inches='tight')
plt.show()