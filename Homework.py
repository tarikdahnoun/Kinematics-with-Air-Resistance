# Homework 5
# Tarik Dahnoun
# Due 9/7/2017

import numpy as n
import pylab as p
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

tinitial=0 #sec
tfinal=8 #sec
nts = 10# number of timesteps
dt = float(tfinal - tinitial)/nts

# Create arrays of values
t = n.linspace(tinitial,tfinal,num=nts+1)
Y = n.zeros(len(t))
V = n.zeros(len(t))
v = n.zeros(len(t))
y = n.zeros(len(t))
y_under = n.zeros(len(t))
error = n.zeros(len(t))

g = 9.8 #m/s^2
Y[0] = 12.0 #meters
V[0] = 35.0 #meters/second
B1=.5

y[0]=12.0
v[0]=35.0


for i in range(0,nts):
    V[i+1] = V[i] - g*dt
    print "At time t = {:.3f}, Velocity = {:.3f}" .format(t[i+1],V[i+1])

print

for j in range(0,nts):
     Y[j+1] = Y[j] + V[j]*dt
     print "At time t = {:.3f}, Position = {:.3f}" .format(t[j+1],Y[j+1])

print
Y_under=Y[0]+V[0]*t-.5*g*t**2  #Analytic Graph
Y_8=Y[0]+V[0]*t[nts]-.5*g*(t[nts]**2)
print "At t=8 seconds, the actual height is y=",Y_8, "and the error is", Y_8-Y[nts]

print

print "Table of Errors"
print
print "Step  |   Error"
table= n.zeros ((nts,2))
for m in range(0,nts):
    error=Y[m]-Y_under[m]
    table = [m,error]
    print table


print"_____________________________________"
print"If we include air resistance"

for k in range(0,nts):
    v[k+1] = v[k] - (B1*v[k]+g)*dt
    print "At time t = {:.3f}, Velocity = {:.3f}" .format(t[k+1],v[k+1])

print

for l in range(0,nts):
    y[l+1] = y[l] + v[l]*dt
    print "At time t = {:.3f}, Position = {:.3f}" .format(t[l+1],y[l+1])



f1 = plt.figure()
p.plot(t,Y_under,"b.-")
ax1 = f1.add_subplot(111)
ax1.plot(t,Y, "r.-")
p.title("Position Graph - Without Air Drag")
p.xlabel("Time (seconds)", fontsize=16)
p.ylabel("Height (meters)", fontsize=16)
red_patch = mpatches.Patch(color='red', label='Approximated Height')
blue_patch = mpatches.Patch(color='blue', label='Analytical Height')
plt.legend(handles=[red_patch,blue_patch])


f2 = plt.figure()
p.plot(t,Y_under, "y.-")
ax2 = f2.add_subplot(111)
ax2.plot(t,y, "g.-")
p.title("Position Graph - With Air Drag")
p.xlabel("Time (seconds)", fontsize=16)
p.ylabel("Height (meters)", fontsize=16)
green_patch = mpatches.Patch(color='green', label='Approximate Height-Air Resistance B=.2')
yellow_patch = mpatches.Patch(color='yellow', label='Analytical Height, B=0') #Same as Blue Graph
plt.legend(handles=[green_patch,yellow_patch])

plt.show()