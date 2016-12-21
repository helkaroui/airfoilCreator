#!/usr/bin/python3.5
try:
    import numpy as np
    import matplotlib.pyplot as plt
except ValueError:
    print("numpy and matplotlib are needed")
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

def main():
    import os
    from argparse import ArgumentParser, RawDescriptionHelpFormatter
    from textwrap import dedent
    parser = ArgumentParser( \
        formatter_class = RawDescriptionHelpFormatter, \
        description = dedent('''\
            Script to generate NACA4 profiles
            If no argument is provided, no demo is displayed.
            '''), \
        epilog = dedent('''\
            Examples:
                Get help
                    python {0} -h
                Generate points for NACA profile 2412
                    python {0} -p 2412
                Generate points for NACA profile 2412 with 300 points
                    python {0} -p 2412 -n 300
                Generate points for NACA profile 2412 and display the result
                    python {0} -p 2412 -d
                Generate points for NACA profile 2412 with smooth points spacing and display the result
                    python {0} -p 2412 -d -s
            '''.format(os.path.basename(__file__))))


    parser.add_argument('-p','--profile', type = str , default = '2412', \
                        help = 'Profile name, default = 2412 . Example: "0009"')
    parser.add_argument('-n','--numberPoints', type = int, default = 500, \
                        help = 'Number of points used to discretize chord. Default is 500.')
    parser.add_argument('-s','--save', type = str, \
                        help = 'Save the generated data to the given filename. Example: -s 2412.data ')
    parser.add_argument('-t','--trailing_edge',type = int , default = 0, \
                        help = 'Finite thickness trailing edge. Default is False, corresponding to zero thickness trailing edge.')
    parser.add_argument('-nd','--not_display', action = 'store_true', \
                        help = 'Flag used to disable display the profile.')
    parser.add_argument('-c','--chord', type = float , default = 1.0 , \
                        help = 'The total length of the chord.')
    parser.add_argument('-pr','--precision',type = int , default = 5, \
                        help = 'The precision of coordinates when saving to file.')
    args = parser.parse_args()

    if args.profile is None:
        print('No argument passed')
    else:
        X , Yc , Xu , Yu , Xl , Yl = naca(args.profile , args.numberPoints , trailing_edge = args.trailing_edge , chord = args.chord)
        if(args.not_display == False):
            plt.plot(X,Yc,Xu,Yu,Xl,Yl)
            plt.grid(True)
            plt.axis('equal')
            plt.show()
        if(args.save is not None):
            # Open a file
            saveFile = open(args.save, "w")
            saveFile.write("NACA"+args.profile+"\n   "+str(args.numberPoints)+"    "+str(args.numberPoints)+"\n");
            for i in range(0,args.numberPoints):
                #Write upper data
                saveFile.write(str(round(Xu[args.numberPoints-1-i],args.precision))+"    "+str(round(Yu[args.numberPoints-1-i],args.precision))+"\n");
            for i in range(1,args.numberPoints):
                #Write upper data
                saveFile.write(str(round(Xl[i],args.precision))+"    "+str(round(Yl[i],args.precision))+"\n");
            saveFile.close()

if __name__ == "__main__":
    main()
