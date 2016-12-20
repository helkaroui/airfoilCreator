#!/usr/bin/python3.5
from NACA_Gen import naca
import matplotlib.pyplot as plt
import numpy as np

nacaType = "2412"
NumberPoints = 500
precision = 9
X , Yc , Xu , Yu , Xl , Yl = naca( nacaType,NumberPoints, trailing_edge = 1, chord = 10)
plt.plot(X,Yc,Xu,Yu,Xl,Yl)
plt.grid(True)
plt.axis('equal')
plt.show()

# Open a file
saveFile = open(nacaType+".dat", "w")
saveFile.write("NACA"+nacaType+"\n");

for i in range(0,NumberPoints):
    #Write upper data
    saveFile.write(str(round(Xu[NumberPoints-1-i],precision))+"    "+str(round(Yu[NumberPoints-1-i],precision))+"\n");
for i in range(1,NumberPoints):
    #Write upper data
    saveFile.write(str(round(Xl[i],precision))+"    "+str(round(Yl[i],precision))+"\n");
saveFile.close()
