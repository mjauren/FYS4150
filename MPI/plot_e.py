import numpy as np
import sys as sys
import matplotlib.pyplot as plt
import os
from matplotlib2tikz import save as tikz_save


J = 1
k_B = 1

if len(sys.argv) < 1:
	print("Please provide filename in commandline")
	sys.exit()
else:
	if sys.argv[1].endswith(".dat"):
		filename = sys.argv[1]
	else:
		filename = sys.argv[1] + ".dat"


T, E, C_V, M, chi, absM = np.loadtxt(filename, unpack = True)

def Z_analytical(T):
    beta = 1/(k_B*T)
    return (4*np.cosh(8*J*beta) + 12)

def E_analytical(T):
    beta = 1/(k_B*T)
    return -32/Z_analytical(T) *np.sinh(8*J*beta)

def C_V_analytical(T):
	beta = 1/(k_B*T)
	Z = Z_analytical(T)
	E = E_analytical(T)
	return beta/T*((256*J**2)/Z * np.cosh(8*beta*J) - E**2)

def M_analytical(T):
	beta = 1/(k_B*T)
	return (16+8*np.exp(8*beta*J))/Z_analytical(T)

def chi_analytical(T):
	beta = 1/(k_B*T)
	M = M_analytical(T)
	Z = Z_analytical(T)
	return beta*(32/Z * (1+np.exp(8*J*beta)) - M**2)


plt.figure()
plt.plot(T, E, 'ro', label='Monte Carlo')
plt.plot(T, E_analytical(T)/4, label='Analytical')
plt.xlabel('Temperature')
plt.ylabel('Energy')
plt.legend()
plt.grid()
tikz_save("../Figures/2Dlattice_E.tex", figureheight="\\figureheight", figurewidth="\\figureheight")

plt.figure()
plt.plot(T, C_V, 'ro', label='Monte Carlo')
plt.plot(T, C_V_analytical(T)/4, label='Analytical')
plt.xlabel('Temperature')
plt.ylabel('Specific heat')
plt.legend()
plt.grid()
#tikz_save("../Figures/2Dlattice_Cv.tex", figureheight="\\figureheight", figurewidth="\\figureheight")

plt.figure()
plt.plot(T, absM, 'ro', label='Monte Carlo')
plt.plot(T, M_analytical(T)/4, label='Analytical')
plt.xlabel('Temperature')
plt.ylabel('Magnetization')
plt.legend()
plt.grid()
#tikz_save("../Figures/2Dlattice_M.tex", figureheight="\\figureheight", figurewidth="\\figureheight")

plt.figure()
plt.plot(T, chi, 'ro', label='Monte Carlo')
plt.plot(T, chi_analytical(T)/4, label='Analytical')
plt.xlabel('Temperature')
plt.ylabel('Susceptibility')
plt.legend()
plt.grid()
#tikz_save("../Figures/2Dlattice_chi.tex", figureheight="\\figureheight", figurewidth="\\figureheight")

plt.show()
