import numpy as np
import matplotlib.pyplot as plt


def y_explicit(x, y0):
    """
    Явна формула розв'язку y(x) для рівняння y' = y^2 - 2y
    з початковою умовою y(0)=y0.
    Повертає None, якщо знаменник → 0 (вертикальна асимптота).
    """
    # Випадки сталих розв'язків
    if abs(y0) < 1e-14:
        return 0.0
    if abs(y0 - 2) < 1e-14:
        return 2.0

    # Загальна формула
    K = (y0 - 2) / y0
    denom = 1 - K * np.exp(2 * x)
    if abs(denom) < 1e-12:
        return None
    return 2.0 / denom


# Початкові умови
y0_plus = 0.5  # b + 1/2 (якщо b=0)
y0_minus = -0.5  # b - 1/2

# Діапазон x (тільки x>=0)
x_vals = np.linspace(0, 5, 500)

# Масиви для збереження розв'язків
Y_plus = []
Y_minus = []
Delta = []

for x in x_vals:
    val_plus = y_explicit(x, y0_plus)
    val_minus = y_explicit(x, y0_minus)
    # Якщо хоч одна з них None -> асимптота
    if val_plus is None or val_minus is None:
        Y_plus.append(np.nan)
        Y_minus.append(np.nan)
        Delta.append(np.nan)
    else:
        Y_plus.append(val_plus)
        Y_minus.append(val_minus)
        Delta.append(abs(val_plus - val_minus))

# Шукаємо перше x, де різниця < 1e-3
x_solution = None
for i, d in enumerate(Delta):
    if not np.isnan(d) and d < 1e-3:
        x_solution = x_vals[i]
        break

if x_solution is not None:
    print(f"Перше x >= 0, де |y(x,0.5)-y(x,-0.5)| < 1e-3: x ≈ {x_solution:.4f}")
else:
    print("Не знайдено x в [0,5], де різниця < 1e-3.")

# Побудуємо графік
plt.figure(figsize=(7, 5))
plt.plot(x_vals, Y_plus, label="y(0)=0.5")
plt.plot(x_vals, Y_minus, label="y(0)=-0.5")
# Вертикальна лінія, де різниця стала < 1e-3
if x_solution is not None:
    plt.axvline(x_solution, color='r', ls='--',
                label=f"x≈{x_solution:.3f}, де |Δ|<1e-3")

plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графіки y(x,0.5) та y(x,-0.5) при x≥0")
plt.legend()
plt.grid(True)
plt.ylim(-2.5, 2.5)
plt.show()
