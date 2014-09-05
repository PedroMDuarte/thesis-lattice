
def rgb_to_hex(rgb):
    #print "Converting color ",rgb
    colorstring = '#' + '{0:02x}'.format(int(255.*rgb[0]))\
		      + '{0:02x}'.format(int(255.*rgb[1]))\
                      + '{0:02x}'.format(int(255.*rgb[2]))
    return colorstring

def cmapCycle( cmap, x , inv=False, lbound=0., ubound=1.):
    # Input x in [lbound, ubound] will be mapped to [0,1] 
    if x < lbound: xmap=0.;
    elif x > ubound: xmap=1.;
    else:
        xmap = (x-lbound) / (ubound-lbound) 
    if inv: 
        xmap = 1.-xmap
    return rgb_to_hex( cmap(xmap) ) 
