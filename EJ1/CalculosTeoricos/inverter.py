from sympy import Symbol
from sympy import Function, simplify
from sympy import *
from sympy import init_printing
from sympy.core.numbers import pi, I, oo
from sympy import re, im
from sympy.solvers.inequalities import solve_rational_inequalities
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy.solvers import solve
import matplotlib.pyplot as plt
import math
import numpy as np

WP = 10 * 2 * np.pi  #o 12Hz
F = 10000 #!!!!!!!!!
VCC = 15
A0 = 112000
VD = 1 #!!!!!!!!!!!
RD = 500000#SIMULAR Y VER!!!!!!!!!!!
R0 = 1#SIMULAR Y VER!!!!!!!!!!


#w = 2*np.pi*F

r1 = Symbol('R1',real = True, positive = True)
r2 = Symbol('R2',real = True, positive = True)
r3 = Symbol('R3',real = True, positive = True)
r4 = Symbol('R4',real = True, positive = True)
a = Symbol('A',real = True, positive = True)
#w = Symbol('w',real = True, positive = True)
#wp = Symbol ('Wpppp',real = True, positive = True)
f = Symbol('f',real = True, positive = True)
#vcc = Symbol('Vcc',real = True, positive = True)
#sr = Symbol('SR',real = True, positive = True)
#vp = Symbol('Vp',real = True, positive = True)
#vin = Symbol('Vin',real = True, positive = True)
vo = Symbol('Vo',real = True, positive = True)
r5 = Symbol('R5',real = True, positive = True)
r6 = Symbol('R6',real = True, positive = True)
raux = Symbol('Raux',real = True, positive = True)

def replaceValues (equation, case, a_):
    equation = equation.subs(a, a_)
    #equation = equation.subs(wp, WP/(2*np.pi))
    #equation = equation.subs(vcc, VCC)
    if case == 1:
        equation = equation.subs(r1, 2500)
        equation = equation.subs(r2, 25000)
        equation = equation.subs(r3, 2500)
        equation = equation.subs(r4, 10000)
    elif case == 2:
        equation = equation.subs(r1, 2500)
        equation = equation.subs(r2, 2500)
        equation = equation.subs(r3, 2500)
        equation = equation.subs(r4, 10000)
    elif case == 3:
        equation = equation.subs(r1, 25000)
        equation = equation.subs(r2, 2500)
        equation = equation.subs(r3, 25000)
        equation = equation.subs(r4, 100000)
    return simplify(equation)


s = Symbol('s')
aw = A0 / (1 + s/WP) #W or wp?

h = - ((r2/r1) / (1 + ((r2/r1)/a) + (1/a) + ((r2/r3)/a)))
h = simplify(h)

hMod = sqrt(re(h)**2 + im(h)**2)
hMod = simplify(hMod)

print("inverter: Vo/Vi=")
result = replaceValues(h, 1, aw) #pasarle A0 o aw dependiendo de lo que quiera analizar.
print("CASO 1>")
print(latex(result.evalf()))

result = replaceValues(h, 2, aw) #pasarle A0 o aw dependiendo de lo que quiera analizar.
print("CASO 2>")
print(latex(result.evalf()))

result = replaceValues(h, 3, aw) #pasarle A0 o aw dependiendo de lo que quiera analizar.
print("CASO3>")
print(latex(result.evalf()))


#ESTO ES CONSIDERANDO R INTERNAS!-----------
#r5 = (r4*R0)/(r4+R0)
#vo = VD * ((a/R0 - 1/r2)/(1/r5 + 1/r2))
#r6 = (vo*R0)/(VD*a)
#raux =(r3 * (r2+((r5*r6)/(r5+r6))))/(r3+r2+((r5*r6)/(r5+r6)))
#zin = r1 + (RD*raux)/(RD+raux)
#HASTA ACAAAAAAAAAAAAA----------------------

#CASO IDEAL:
zin_sp = (a*r1 + r1 + r2)/(1+a)
rp=10000000
cp=1/(s * 12e-12)
puntas = (rp * cp)/(rp+cp)
zin = (puntas * zin_sp)/(puntas + zin_sp)

result = replaceValues(zin_sp, 1, aw)
print("inverter: Zin caso1=")
print(latex(result.evalf()))

result = replaceValues(zin_sp, 2, aw)
print("inverter: Zin caso2=")
print(latex(result.evalf()))

result = replaceValues(zin_sp, 3, aw)
print("inverter: Zin caso3=")
print(latex(result.evalf()))
