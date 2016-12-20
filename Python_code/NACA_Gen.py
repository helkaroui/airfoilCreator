#!/usr/bin/python3.5
import numpy as np
# naca generator Function definition
def naca(nacaType , NumberPoints , trailing_edge = 0 , chord = 1):
    """This function takes as Inputs
    nacaType : String
    NumberPoints : Integer
    trailing_edge : Boolean
    """
    if len(nacaType) != 4:
        return;
    M = int(nacaType[0])/100
    P = int(nacaType[1])/10
    T = int(nacaType[2:])/100
    # Constants used in thickness calculation
    a0 = 0.2969;
    a1 = -0.1260;
    a2 = -0.3516;
    a3 = 0.2843;

    if (trailing_edge == 0):
        #Open trailing edge
        a4 = -0.1015;
    elif(trailing_edge == 1):
        #Closed trailing edge
        a4 = -0.1036;
    X = np.linspace(0,1,NumberPoints)
    # Camber
    Yc = np.ones((NumberPoints))
    dYc = np.ones((NumberPoints))
    theta = np.ones((NumberPoints))
    for i in range(0,NumberPoints):
        if (X[i] < P):
            Yc[i]= (M/P**2)*(2*P*X[i] - X[i]**2)
            dYc[i] = ((2*M)/(P**2))*(P-X[i])
        elif (X[i] > P):
            Yc[i]= (M/(1-P)**2)*( 1 - 2*P  + 2*P*X[i] - X[i]**2);
            dYc[i] = ((2*M)/((1-P)**2))*(P-X[i]);
        theta[i] = np.arctan(dYc[i]);
    Yt = np.ones((NumberPoints));
    Yt = 5*T*((a0 * np.sqrt(X)) + (a1*X) + (a2 * X**2) + (a3 * X**3 ) + (a4 * X**4 ));

    # Upper Points
    Xu = np.ones((NumberPoints));
    Yu = np.ones((NumberPoints));

    Xu = X - Yt * np.sin(theta);
    Yu = Yc + Yt * np.cos(theta);


    # Lower Points
    Xl = np.ones((NumberPoints));
    Yl = np.ones((NumberPoints));

    Xl = X + Yt * np.sin(theta);
    Yl = Yc - Yt * np.cos(theta);
    return chord*X , chord*Yc , chord*Xu , chord*Yu , chord*Xl , chord*Yl
