import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 10)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x*x))       # Plot the sine of each x point
plt.show()                   # Display the plot

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x*x))       # Plot the sine of each x point
plt.show()    

x = np.linspace(0, 20, 1000)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x*x))       # Plot the sine of each x point
plt.show()    
