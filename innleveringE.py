import pandas as pd
import numpy as np

# prosentandel nordmenn som har kontakt med innvandrere
kontakt = pd.read_csv('kontakt.csv', index_col=0, comment='#')

# prosentandel nordmenn som har positiv holdning til innvandrere
holdning = pd.read_csv('holdning.csv', index_col=0, comment='#')

# Nedbor (mm) i januar fra 1890 til 1994
nedbor = pd.read_csv('nedbor.csv', index_col=0, comment='#')

# Nedbør
Sx = np.var(nedbor.index.values.flatten())
Sy = np.var(nedbor.values.flatten())
Sxy = np.cov(nedbor.index, nedbor.values.flatten())[0][1]

print("nedbør:", "Sx:", Sx, "Sy:",Sy, "Sxy:", Sxy)

#innvandrere. Kontakt er X-aksen.

Sx = np.var(kontakt.values.flatten())
Sy = np.var(holdning.values.flatten())
Sxy = np.cov(kontakt.values.flatten(), holdning.values.flatten())[0][1]

print("innvandring:", "Sx:", Sx, "Sy:", Sy, "Sxy:", Sxy)


#print(np.corrcoef(x, y)[0][1])

#print(np.corrcoef(holdning.values.flatten(), kontakt.values.flatten())[0][1])
