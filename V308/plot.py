import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy.optimize as opt




BH1, IH1, H1, M1 = np.genfromtxt('Hysterese1.txt', unpack=True)
BH2, IH2, H2, M2 = np.genfromtxt('Hysterese2.txt', unpack=True)
BH3, IH3, H3, M3 = np.genfromtxt('Hysterese3.txt', unpack=True)
plt.plot(H1, BH1, 'r-', label='erste Kurve')
plt.plot(H1, BH1, 'rx')
plt.plot(H2, BH2, 'b-', label='zweite Kurve')
plt.plot(H2, BH2, 'bx')
plt.plot(H3, BH3, 'g-', label='dritte Kurve')
plt.plot(H3, BH3, 'gx')
plt.grid(True)
plt.plot([0,0], [129.0, -123.6], 'm*', label='Remanenz')
plt.plot([370,-370], [0,0], 'c*', label='Koerzitivkraft')
plt.plot([-7018.2,7018.2], [-713.2,718], 'y*', label='Sättigung')

plt.axis([-8000, 8000, -800, 800])
plt.xlabel(r'H/(A/m)')
plt.ylabel(r'$B/$mT')
plt.legend(loc='best')
plt.savefig('plot5.pdf')












