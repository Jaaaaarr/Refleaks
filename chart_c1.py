# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:39:03 2017

@author: ja-man
"""
import numpy as np
import matplotlib.pyplot as plt

# Refrigerant Dictionary

r1234yf = {"molmass":114, "reldensity":3.75, "expansionratio":1.253, "flashpoint":None,
           "AIT":405, "bp":-21, "vp20":1518.92, "LFL":6.2}  

print("\n\n\n===== Degree of Dilution Plot =====\nNote: R1234yf assumed")
uw = input("\nType in ventilation velocity [m/s]: ")
Wg = 0.001 * float(input("\nType in release rate [g/s]: "))

rhog = 3.25
k = 0.25
LFL = 6.0 * 0.01

def f1(blue):
  return 14 * (blue**1)
def f2(red):
  return 0.045 * (red**1)

#x1 = np.arange(0.001, 100, 0.001)
x1 = np.geomspace(0.001, 100, 50)

plt.figure()
plt.suptitle("Assessment of degree of dilution", fontsize = 12)
plt.grid(True)

plt.xlabel("Release characteristic Wg / rhog * k * LFL [m3/s]")
plt.xscale("log")

plt.ylabel("Ventilation velocity Uw [m/s]")
plt.yscale("log")

plt.plot(x1, f1(x1), "b", x1, f2(x1), "r")
#plt.show()

Rc = Wg / (rhog * k * LFL)

#print("Rc = " + str(Rc))

marker_pos = [(Wg / (rhog * k * LFL)), uw]
plt.plot(marker_pos[0], marker_pos[1], "o")

""" det numerically"""

# Let x = Wg
if float(marker_pos[1]) <= f2(Rc):
  dilutiondegree = "Low dilution"
  colour = "red"
elif float(marker_pos[1]) >= f1(Rc):
  dilutiondegree = "High dilution"
  colour = "blue"
else:
  dilutiondegree = "Medium dilution"
  colour = "green"
  
plt.title(dilutiondegree, fontsize = 15, color = colour)
print("The dilution is assessed to be that of a " + dilutiondegree)