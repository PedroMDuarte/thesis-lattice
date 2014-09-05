import numpy as np
from scipy.interpolate import interp1d
#Here the interpolation data is loaded from disk
v0 = np.loadtxt('banddat/interpdat_B1D_v0.dat')
NPoints = 5
interp0 = []
interp1 = []
for n in range( 2*NPoints+1 ):
    interp0.append( interp1d(v0, np.loadtxt('banddat/interpdat_B1D_0_%d.dat'%n) ))
    interp1.append( interp1d(v0, np.loadtxt('banddat/interpdat_B1D_1_%d.dat'%n) ))
    
def bands3dinterp( v0, NBand=0 ):
    r"""Returns an array of shape (2,) which has the bottom and top of the band energies

    Given the lattice depth it will calculate the bottom and the
    top of the band with band index equal to NBand.
    
    Parameters
    ----------
    v0 : array-like
        len(v0) must be equal to 3.  Each entry corresponds to the
        lattice depth in recoils along x, y, z respectively
    NBand : 
        band index (default = 0 )

    Returns
    -------
    array-like
        array of shape (2,) which has the bottom of the band as 
        first entry and the top of the band as second entry.
    """
    assert len(v0)==3
    order = np.argsort( v0 )
    l=0; m=0; n=0
    while NBand > 0:
        l+=1; NBand-=1
        if NBand > 0:
            m+=1; NBand-=1
        if NBand > 0:    
            n+=1; NBand-=1
    band1dindex = np.array([ l, m, n] )
        
    bandbot = 0. 
    bandtop = 0. 
    for i,o in enumerate(order):
        in1d = band1dindex[i]
        if in1d%2 ==0:
            bandbot += interp0[in1d](v0[o]) 
            bandtop += interp1[in1d](v0[o])
        else:
            bandbot += interp1[in1d](v0[o])
            bandtop += interp0[in1d](v0[o])
    return np.array([bandbot, bandtop])


def bands3dinterpvec( v0, NBand=0):
    r""" Returns an array of shape (len(v0,2) which has the bottom and 
    top of the band energies

    Parameters
    ----------
    v0 : array-like
        The shape of v0 is (len(v0,3).  Each row of v0 has 3
        values.  Each value corresponds to the lattice depth 
        in recoils along x, y, z respectively. 
    NBand : optional
        Band index (default = 0 )
    """
    band = np.empty( (len(v0), 2) ) 
    for i,v in enumerate(v0):
        band[i] = bands3dinterp(v, NBand)
    return band

def hosc3d( NBand, v0 ):
    r"""Energy of the NBand^th excited state of the 3D harmonic oscillator"""
    return 2* np.sqrt(  v0 ) * (NBand + 1.5)
