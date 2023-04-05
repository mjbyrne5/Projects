import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
from sympy import pretty_print

x = smp.Symbol("x")
n = smp.Symbol("n", positive=True)
T = smp.pi
f = x
g = smp.pi - x
f1 = (2/T) * f * smp.cos((2*smp.pi*n*x)/T)
g1 = (2/T) * g * smp.cos((2*smp.pi*n*x)/T)
f2 = (2/T) * f * smp.sin((2*smp.pi*n*x)/T)
g2 = (2/T) * g * smp.sin((2*smp.pi*n*x)/T)

A0f = smp.integrate(f, x)
A0g = smp.integrate(g, x)


def definite(a, b):
  return A0f.evalf(subs={x: b}) - A0f.evalf(subs={x: a})


def definite1(a, b):
  return A0g.evalf(subs={x: b}) - A0g.evalf(subs={x: a})


A0f = (1/T) * definite(0, smp.pi/2)
A0g = (1/T) * definite1(smp.pi/2, smp.pi)
A0 = A0f + A0g

Anf = smp.integrate(f1, x)
Ang = smp.integrate(g1, x)


def definiteAnf(a, b):
  return Anf.evalf(subs={x: b}) - Anf.evalf(subs={x: a})


def definiteAng(a, b):
  return Ang.evalf(subs={x: b}) - Ang.evalf(subs={x: a})


Anf = definiteAnf(0, smp.pi/2)
Ang = definiteAng(smp.pi/2, smp.pi)
An = Anf + Ang

Bnf = smp.integrate(f2, x)
Bng = smp.integrate(g2, x)


def definiteBnf(a, b):
  return Bnf.evalf(subs={x: b}) - Bnf.evalf(subs={x: a})


def definiteBng(a, b):
  return Bng.evalf(subs={x: b}) - Bng.evalf(subs={x: a})


Bnf = definiteBnf(0, smp.pi/2)
Bng = definiteBng(smp.pi/2, smp.pi)
Bn = Bnf + Bng

final = (An * smp.cos((2*smp.pi*n*x)/T)) + (Bn * smp.sin((2*smp.pi*n*x)/T))
pretty_print(final)  # Does not include A0

x = np.linspace(0, 10, num=100)
y = np.zeros(len(x))
count = 0

for j in range(1, 6):
    print(f'{j} finished')
    count = 0
    for i in x:
        z = final.evalf(subs={'x': i, n: j})
        y[count] = y[count] + z
        count += 1

y = y + A0

plt.plot(x, y)
plt.show()
