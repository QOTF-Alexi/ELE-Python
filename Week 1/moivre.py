from math import pi, cos, sin
from fractions import Fraction
α = Fraction(1,4)*pi
n = 5
moivre1 = (cos(α)+1j*sin(α))*n
moivre2 = cos(n*α)+1j*sin(n*α)
print(moivre1, '=', moivre2)