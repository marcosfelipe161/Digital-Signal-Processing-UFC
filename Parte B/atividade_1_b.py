import numpy as np
import matplotlib.pyplot as plt

# Parte B: Frequência digital e periodicidade
n_b = np.arange(0, 81)
xa = np.cos((np.pi / 2) * n_b)
xb = np.cos((np.pi * np.sqrt(2) / 2) * n_b)

plt.figure(figsize=(8, 4))
plt.stem(n_b, xa)
plt.title('xa[n] = cos(pi*n/2) - Periódico')
plt.grid(True)

plt.figure(figsize=(8, 4))
plt.stem(n_b, xb)
plt.title('xb[n] = cos(pi*sqrt(2)*n/2) - Aperiódico')
plt.grid(True)

plt.show()
