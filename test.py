import numpy as np
import matplotlib.pyplot as plt

# Створення масиву значень x від 0 до 1/sqrt(2)
x = np.linspace(0, 1/np.sqrt(2), 200)

# Обчислення значень функції щільності: f(x) = 2√2 - 4x
f = 2 * np.sqrt(2) - 4 * x

# Створення графіка
plt.figure(figsize=(8, 6))
plt.plot(x, f, lw=2, color='blue', label=r'$f(x)=2\sqrt{2}-4x$')

# Позначення осей та заголовку
plt.xlabel('x', fontsize=14)
plt.ylabel('f(x)', fontsize=14)
plt.title('Графік функції щільності', fontsize=16)

# Додавання осей (x=0 та y=0) чорним кольором
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Налаштування розміру шрифтів для підписів осей
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Додавання легенди
plt.legend(fontsize=12)

# Додавання сітки
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.show()
