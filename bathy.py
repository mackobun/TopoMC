# bathy module

import numpy
from itertools import product
from random import random

def getBathymetry(lcArray, maxDepth, slope=1):
    "Generates rough bathymetric values based on proximity to terrain.  Increase slope to decrease dropoff."
    bathyMaxRows, bathyMaxCols = lcArray.shape
    bathyArray = numpy.zeros((bathyMaxRows, bathyMaxCols))
    for brow, bcol in product(xrange(bathyMaxRows), xrange(bathyMaxCols)):
        if (lcArray[brow,bcol] == 11):
            bxmin = max(0, brow-1)
            bxmax = min(bathyMaxRows,brow+2)
            bzmin = max(0, bcol-1)
            bzmax = min(bathyMaxCols,bcol+1)
            barray = bathyArray[bxmin:bxmax,bzmin:bzmax].flatten()
            bathyList = [int(x) for x in barray]
            if (all(element == 0 for element in bathyList)):
                ringrange = xrange(1,maxDepth)
            else:
                ringrange = xrange(min([elem for elem in bathyList if elem > 0])-1,min(max(bathyList)+2, maxDepth))
            try:
                for ring in ringrange:
                    if (True):
                        if any(lcArray[ringrow,ringcol] != 11 for ringrow in xrange(max(0, brow-ring+1), min(bathyMaxRows, brow+ring+1)) for ringcol in xrange(max(0, bcol-ring+1), min(bathyMaxCols, bcol+ring+1))):
                            raise Exception
                    else:
                        xmin = max(0, brow-ring+1)
                        xmax = min(bathyMaxRows, brow+ring+1)
                        zmin = max(0, bcol-ring+1)
                        zmax = min(bathyMaxCols, bcol+ring+1)
                        ringarray = lcArray[xmin:xmax,zmin:zmax]
                        if any(x != 11 for x in ringarray):
                            raise Exception
            except Exception:
                pass
            if (random() > 1/slope):
                ring = ring + 1
            bathyArray[brow,bcol] = ring
    return bathyArray

