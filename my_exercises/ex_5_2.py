import numpy as np
import matplotlib.pyplot as plt

import scipy.stats
import random

def func(x):
    return np.exp(-x**2/2)

def q(x):
    return 3*np.exp(-x**2/2)

def sampling(x):
    return random.uniform(0,q(x))

rng = np.random.default_rng(42)

n=100
x_plot = np.linspace(-5,5,500)

x_r=rng.uniform(-5, 5, n)
u=[]
for i in range(0,n):
    u.append(sampling(x_r[i]))

counts = np.sum(u <= func(x_r))

points_good=[[],[]]
points_bad=[[],[]]

for i in range(0,n):
    if u[i] <= func(x_r[i]):
        points_good[0].append(x_r[i])
        points_good[1].append(u[i])
    else:
        points_bad[0].append(x_r[i])
        points_bad[1].append(u[i])

plt.plot(x_plot, func(x_plot), label='$p(x)$')
plt.plot(x_plot,q(x_plot), label='$Mq(x)$')
#plt.hist(counts, density=True, alpha=0.5, label=rf"Samples, $n={n}$")

plt.scatter(points_good[0],points_good[1], color='blue')
plt.scatter(points_bad[0],points_bad[1], color='grey')

plt.legend()
plt.show()
