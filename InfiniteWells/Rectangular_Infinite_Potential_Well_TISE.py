#!/usr/bin/env python
# coding: utf-8

# In[58]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d


# In[72]:


# define constants

N = 8 # state of the wavefunction

L_x = 1 # width of the potential well in x-direction
A_x = np.sqrt(2 / L_x) # normalisation constant for x-component of wavefunction

L_y = 1 # width of the potential well in y-direction
A_y = np.sqrt(2 / L_y) # normalisation constant for y-component of wavefunction


# In[73]:


x = np.linspace(0,1,1000)
y = np.linspace(0,1,1000)

X, Y = np.meshgrid(x, y)

def wavefunction (x, y, n):
    """
    Returns the value of the analytic solution to the Schrodinger equation
    for a particle in a two-dimensional infinite potential well at the point
    (x, y). The integer n describes the state of the wavefunction. 
    """
    return (A_x * A_y) * np.sin(x * n * np.pi / L_x) * np.sin(y * n * np.pi / L_y)


def probDist (x, y, n):
    """
    Returns the probability of a particle in a two-dimensional infinite potential 
    existing at a point (x, y). This is used to find the probability distribution
    The integer n describes the state of the wavefunction.
    """
    return wavefunction(x, y, n)**2

psi = wavefunction(X, Y, N) 
prob = probDist(X, Y, N)


# In[76]:


get_ipython().run_line_magic('matplotlib', 'notebook')
fig1 = plt.figure()      

ax1 = plt.axes(projection='3d')
ax1.contour3D(X, Y, psi, 50, cmap='binary') # plotting the probability distribution 


# In[75]:


fig2 = plt.figure()

ax2 = plt.axes(projection = '3d')
ax2.contour3D(X, Y, prob, 50, cmap='binary') # plotting the probability distribution 


# In[ ]:





# In[ ]:





# In[ ]:




