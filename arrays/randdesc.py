import scipy as sp
import scipy.constants

# This antenna is an 18-element random array, with Z and Y coordinates from the
# file "randarray_inches.dat
# Operating frequency is 2.4771 GHz.

numel = 18

wl = sp.constants.c / 2.4771e9

zy = sp.loadtxt("randarray_inches.dat")

arr_in = sp.array((sp.zeros(numel),zy[:,1],zy[:,0])).T

arr_m = 0.054 * arr_in

arr = arr_m / wl

#Interleave polarizations
doubled = []
for ant in arr:
    doubled.append(ant)
    doubled.append(ant)

sp.savetxt("randarray.dat", sp.array(doubled))
