#This line imports the pyplot module from the matplotlib library and assigns it the alias plt
import matplotlib.pyplot as plt

#Here you write the coordinates 
x=[1,4,7,9]
y=[2,3,6,5]

# This line plots the data points using the plot() function
plt.plot(x,y,)

#This will give the names to the x-axis and y-axis
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

#This line sets the title of the plot as "A simple line graph".
plt.title("A simple line graph")

#This line displays the plot on the screen.
plt.show()
