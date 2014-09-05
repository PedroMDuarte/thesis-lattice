# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Here the interpolation data is loaded from disk
from scipy.interpolate import interp1d
tInterp = interp1d( np.loadtxt('banddat/interpdat_t_v0.dat'), np.loadtxt('banddat/interpdat_t_tCalc.dat'))

from scipy.interpolate import interp1d
wFInterp = interp1d( np.loadtxt('banddat/interpdat_wF_v0.dat'), np.loadtxt('banddat/interpdat_wF_wF.dat'))

def U_over_t( v0, a ):
    a0a =  5.29e-11 / (1064e-9/2)
    U = a*a0a*wFInterp(v0)
    t = tInterp(v0)
    return U/t

# <codecell>

U_over_t( 7., 200.)

# <codecell>

tInterp(7.)

# <codecell>

3.5*0.04

# <codecell>


