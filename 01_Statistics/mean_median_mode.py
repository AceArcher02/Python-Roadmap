import statistics
import numpy 
speed=[99,87,98,65,77,87]

x=numpy.mean(speed)
print("Mean:",x)

y=numpy.median(speed)
print("Median:",y)

z=statistics.mode(speed)
print("Mode:",z)
