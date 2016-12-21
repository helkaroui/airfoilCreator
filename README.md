# airfoilCreator
![](https://people.sc.fsu.edu/~jburkardt/m_src/naca/symmetric.png)
naca4.py is a script to generate NACA4 profiles. If no argument is provided, no demo is displayed.

optional arguments:

  -h, --help            show this help message and exit

  -p, --profile : Profile name, default = 2412 . Example: "0009"
  
  -n, --numberPoints : Number of points used to discretize chord. Default is 500.
  
  -s SAVE, --save SAVE  Save the generated data to the given filename. Example: -s 2412.data
  
  -nd, --not_display    Flag used to disable display the profile.
  
  -c CHORD, --chord           set the total length of the chord.
  
  -pr PRECISION, --precision  set the precision of coordinates when saving to file.
  
  Example:
  
  `naca4.py -p 2412 -s 2412.data`
