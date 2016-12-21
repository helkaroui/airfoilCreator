# airfoilCreator

https://github.com/helkaroui/airfoilCreator/wiki

naca4.py is a script to generate NACA4 profiles. If no argument is provided, no demo is displayed.

optional arguments:

  -h, --help            show this help message and exit

  -p, --profile : Profile name, default = 2412 . Example: "0009"
  
  -n, --numberPoints : Number of points used to discretize chord. Default is 500.
  
  -s SAVE, --save SAVE  Save the generated data to the given filename. Example: -s 2412.data
  
  -nd, --not_display    Flag used to disable display the profile.
  
  -c CHORD, --chord           set the total length of the chord.
  -pr PRECISION, --precision  set the precision of coordinates when saving to file.

Examples:
    Get help
        python naca4.py -h
    Generate points for NACA profile 2412
        python naca4.py -p 2412
    Generate points for NACA profile 2412 with 300 points
        python naca4.py -p 2412 -n 300
    Generate points for NACA profile 2412 and desable displaying the result
        python naca4.py -p 2412 -nd
    Generate points for NACA profile 2412 And save the generated data to the given filename.
        python naca4.py -p 2412 -d -s result.data
    Generate points for NACA profile 2412 And set the chord length to 10.
        python naca4.py -p 2412 -c 10
