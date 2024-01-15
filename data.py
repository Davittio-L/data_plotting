import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fix, ax = plt.subplots() #Common matplotlib convention - calling the subplots() function. This function can generate oone or more plots in the same figure. 
# The variable 'fig' represents the entire figure or collection of plots that will be generated. The variable 'ax' represents a single plot in the figure and is the variable we'll use most of the time.
ax.scatter(2, 4)
ax.plot(input_values, squares, linewidth=3)

# ax.plot(squares, linewidth=3)

# Set chart title and label axes.

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show() #using the plot method to attempt to plot data. 

