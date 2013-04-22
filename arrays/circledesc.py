import scipy as sp
import scipy.constants

# This antenna is an 18-element circular array, with radius 12.5 in
# operating at 2.4771 GHz

numel = 18

wl = sp.constants.c / 2.4771e9

rad = 0.0254*12.5

arr = [ 
        (0,rad*sp.cos(th), rad*sp.sin(th)) 
        for th in sp.linspace(0, 2*sp.pi, numel, endpoint=False) 
      ]

#Interleave polarizations
doubled = []
for ant in arr:
    doubled.append(ant)
    doubled.append(ant)

sp.savetxt("circarray.dat", sp.array(doubled))
