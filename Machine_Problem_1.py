#Machine Problem 1 (Piecewise Funtion)
from matplotlib import pyplot as plot #Used for Plotting the function and using STEM
def function (n): #Defining the Function
#IF Statements 
    if n <= 9:
        return (n**2) - 7 #First Function
    else:
        return function(n-10) #Second Function
#Storage for different Values
x = []
y = []
#For Loop
for i in range(0,100):
    x.append(i) #Values of i is stored to the Initialized list of X
    y.append(function(i)) #Values of i is stored to the Initialized list of Y
#Plotting Using Stem and its Attributes
plot.stem(x, y, use_line_collection=True, markerfmt='x') 
plot.title('The Function and Its Graph') 
plot.xlabel('X-Axis'); plot.ylabel('Y-Axis')
plot.show()