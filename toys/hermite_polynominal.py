import numpy as np
import sympy
import matplotlib.pyplot as plt
import math

plt.rcParams['font.size'] = 14
# plt.rcParams['font.family'] = 'Harano Aji Mincho'
plt.rcParams['text.usetex'] = True  # Use TeX for rendering
plt.rcParams['font.family'] = 'serif'  # Set the font to a serif type, which is common in TeX documents

# plt.rcParams['xtick.direction'] = 'none'
# plt.rcParams['ytick.direction'] = 'none'
fig = plt.figure(figsize=(8, 5))
ax1 = fig.add_subplot(111)
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['left'].set_position(('data', 0))
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.plot(1, 0, ">k", transform=ax1.get_yaxis_transform(), clip_on=False)
ax1.plot(0, 1, "^k", transform=ax1.get_xaxis_transform(), clip_on=False)
ax1.text(5.4, -1, r"$x$", fontsize=16, ha='center')
ax1.text(1, 24.2, r"$E_n, |\psi_n(x)|^2$", fontsize=16, ha='center')
ax1.text(0.5, -1.2, r"$O$", fontsize=16, ha='center')
plt.xticks([])
plt.yticks([])

n = 10
x = sympy.Symbol('x')
h = [(np.pi ** (-1 / 4)) * sympy.exp(- x ** 2 / 2)]
for i in range(n):
    nw = (1 / math.sqrt(2 * (i + 1))) * (x * h[i] - sympy.diff(h[i]))
    h.append(nw)
    print(nw)
    # print(sympy.integrate(nw ** 2, (x, - sympy.oo, sympy.oo)))
h_numeric = [sympy.lambdify(x, func, "numpy") for func in h]
xk = np.linspace(-4.8, 4.8, 400)
for i, func in enumerate(h_numeric):
    yk = func(xk) + 2 * (i + 0.5)
    yk2 = func(xk) ** 2 + 2 * (i + 0.5)
    # plt.plot(xk, yk, color = "b")
    plt.hlines(2 * (i + 0.5), -4.8, 4.8, color = "k", linestyle='--')
    plt.plot(xk, yk2, color = "r")
    plt.text(5, 2 * (i + 0.2), rf"$n = {i}$")
plt.plot(xk, xk ** 2, color = "k")
plt.savefig("hermite-rev.pdf", bbox_inches = "tight")
plt.show()
plt.close()
