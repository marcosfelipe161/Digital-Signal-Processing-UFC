import numpy as np
import matplotlib.pyplot as plt

# Parte A: Geração e visualização
n_a = np.arange(0, 21)
x1 = np.ones_like(n_a)
x2 = 0.8**n_a
x3 = np.sin(0.3 * np.pi * n_a)

for x, name in [(x1, 'x1[n] = 1'), 
                (x2, 'x2[n] = 0.8^n'), 
                (x3, 'x3[n] = sin(0.3*pi*n)')]:
    plt.figure(figsize=(8, 4))
    plt.stem(n_a, x)
    plt.title(name)
    plt.grid(True)

plt.show()
