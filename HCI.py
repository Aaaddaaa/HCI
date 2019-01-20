import numpy as np
import aseegg as ag
import pandas as pd
import matplotlib.pyplot as plt
dane = pd.read_csv("sub-01_trial-112.csv", delimiter=';', engine='python')

result = dane["p1"]
numer = dane["numer"]
czestProbkowania = 200

t = np.linspace(0, 37, 37*200)

sygnal = np.sin(2* np.pi* czestProbkowania *t)


dane.head()
plt.plot(t, sygnal)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda[-]")
plt.show()
