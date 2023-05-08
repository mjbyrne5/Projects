import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
from sympy import pretty_print

# Symbols
x = smp.Symbol("x")
n = smp.Symbol("n", positive=True)

# Set period length
T = smp.pi

# Functions
f = x
g = smp.pi/2 - x
p = x - smp.pi/2

f1 = (2/T) * f * smp.cos((2*smp.pi*n*x)/T)
f2 = (2/T) * f * smp.sin((2*smp.pi*n*x)/T)
g1 = (2/T) * g * smp.cos((2*smp.pi*n*x)/T)
g2 = (2/T) * g * smp.sin((2*smp.pi*n*x)/T)
p1 = (2/T) * p * smp.cos((2*smp.pi*n*x)/T)
p2 = (2/T) * p * smp.sin((2*smp.pi*n*x)/T)

A0f = smp.integrate(f, x)
A0g = smp.integrate(g, x)
A0p = smp.integrate(p, x)


def definite(a, b):
    return A0f.evalf(subs={x: b}) - A0f.evalf(subs={x: a})


def definite1(a, b):
    return A0g.evalf(subs={x: b}) - A0g.evalf(subs={x: a})


def definite2(a, b):
    return A0p.evalf(subs={x: b}) - A0p.evalf(subs={x: a})


# Update to reflect period
A0f = (1/T) * definite(0, smp.pi/4)
A0g = (1/T) * definite1(smp.pi/4, smp.pi/2)
A0p = (1/T) * definite2(smp.pi/2, smp.pi)
A0 = A0f + A0g + A0p

Anf = smp.integrate(f1, x)
Ang = smp.integrate(g1, x)
Anp = smp.integrate(p1, x)

# Ignore function squigglies, they work


def definiteAnf(a, b):
    return Anf.evalf(subs={x: b}) - Anf.evalf(subs={x: a})


def definiteAng(a, b):
    return Ang.evalf(subs={x: b}) - Ang.evalf(subs={x: a})


def definiteAnp(a, b):
    return Anp.evalf(subs={x: b}) - Anp.evalf(subs={x: a})


Anf = definiteAnf(0, smp.pi/4)
Ang = definiteAng(smp.pi/4, smp.pi/2)
Anp = definiteAnp(smp.pi/2, smp.pi)
An = Anf + Ang + Anp

Bnf = smp.integrate(f2, x)
Bng = smp.integrate(g2, x)
Bnp = smp.integrate(p2, x)


def definiteBnf(a, b):
    return Bnf.evalf(subs={x: b}) - Bnf.evalf(subs={x: a})


def definiteBng(a, b):
    return Bng.evalf(subs={x: b}) - Bng.evalf(subs={x: a})


def definiteBnp(a, b):
    return Bnp.evalf(subs={x: b}) - Bnp.evalf(subs={x: a})


Bnf = definiteBnf(0, smp.pi/4)
Bng = definiteBng(smp.pi/4, smp.pi/2)
Bnp = definiteBnp(smp.pi/2, smp.pi)
Bn = Bnf + Bng + Bnp

final = (An * smp.cos((2*smp.pi*n*x)/T)) + (Bn * smp.sin((2*smp.pi*n*x)/T))
pretty_print(A0 + final)

# Graph, a higher linspace num or summation range will drastically increase processing time
x = np.linspace(0, 7, num=1000)
y = np.zeros(len(x))
count = 0

# Set range to desired number of iterations + 1, note processing time
for j in range(1, 101):
    print(f'{j} finished')
    count = 0
    for i in x:
        z = final.evalf(subs={'x': i, n: j})
        y[count] = y[count] + z
        count += 1

y = y + A0

plt.plot(x, y)
plt.title('Function as Fourier Series')
plt.show()
