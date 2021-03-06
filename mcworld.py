# minecraft world
import os
import shutil
from pymclevel import mclevel
import logging
logging.basicConfig(level=logging.WARNING)
mcworldlogger = logging.getLogger('mcworld')

world = None

def myinitWorld(string):
    "Open this world."
    global world
    # it's a simpler universe now
    worlddir = os.path.join("Worlds", string)
    if os.path.isdir(worlddir):
        shutil.rmtree(worlddir)
    if not os.path.exists(worlddir):
        os.makedirs(worlddir)
    else:
        raise IOError, "%s already exists" % worlddir

    world = mclevel.MCInfdevOldLevel(worlddir, create=True)

def mysaveWorld():
    global world
    sizeOnDisk = 0
    # stolen from pymclevel/mce.py
    numchunks = 0
    for i, cPos in enumerate(world.allChunks, 1):
        ch = world.getChunk(*cPos);
        numchunks += 1
        sizeOnDisk += ch.compressedSize();
    mcworldlogger.info('%d chunks enumerated' % numchunks)
    world.SizeOnDisk = sizeOnDisk
    world.saveInPlace()

