import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


Xbar = 74.5
n = 104
s = 49.4
my0 = 70
alpha = 0.05
Za = -norm.ppf(alpha, 0, 1)
# Dette er alpha-kvantilen til G. Av en eller annen grunn gir den negativt tall så vi må snu den.

print(Za)

# x-aksen går fra my0-10 til my0+20. Altså fra 60 til 90. Vilkårlig valgt.
x_axis = np.arange(my0 - 10, my0 + 20, 0.001)

# norm.cdf(x, 0, 1) er Gauss-funksjonen for en gitt x.
plt.plot(x_axis, 1 - norm.cdf(Za - (x_axis - my0)/(s/(n**0.5)), 0, 1))
plt.xlabel("mm regn som måles")
plt.ylabel("Sannsynlighet for at H0 forkastes (my > 70)")
plt.show()
