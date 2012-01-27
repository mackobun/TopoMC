from newterrain import Terrain

class L01_Terrain(Terrain):
    """Example class for NLCD 2001."""

    # land cover constants
    # (see http://www.epa.gov/mrlc/definitions.html among others)
    # what portion of developed land should be stone versus grass
    # 21: <20, 22: 20-49, 23: 50-79, 24: 80-100
    level21stone = 0.10
    level22stone = 0.35
    level23stone = 0.65
    level24stone = 0.90
    # what portion of barren land should be stone versus sand
    # no real values inferred
    level31stone = 0.50
    # forest: trees > 5m tall, canopy 25-100%
    # what portion of mixed forest is deciduous versus evergreen
    # 43: neither deciduous nor evergreen is greater than 75 percent
    level43tree0 = 0.50
    # shrubland: trees < 5m tall
    level51stone = 0.25
    level52stone = 0.25
    level73stone = 0.90
    level74stone = 0.90
    # what percentage of wetlands should be grass (versus water)
    wetlandsgrass = 0.80

    # 0: default

    def L01_0(crustval, bathyval):
        #return Terrain.placedirt(crustval)
        return [crustval, 'Obsidian']

    # 10: water

    # 11: water
    # NB: consider lily pad placement?
    def L01_11(crustval, bathyval):
        return Terrain.placewater(crustval, bathyval)

    # 12: perennial ice/snow
    # (is this ever on mountaintops?)
    def L01_12(crustval, bathyval):
        return Terrain.placewater(crustval, bathyval, ice=True)

    # 20: developed

    # 21: developed/open space
    # 0-20 % coverage
    def L01_21(crustval, bathyval):
        return Terrain.placedeveloped(crustval, L01_Terrain.level21stone)

    # 22: developed/low intensity
    # 20-49 % coverage
    def L01_22(crustval, bathyval):
        return Terrain.placedeveloped(crustval, L01_Terrain.level22stone)

    # 23: developed/medium intensity
    # 50-79 % coverage
    def L01_23(crustval, bathyval):
        return Terrain.placedeveloped(crustval, L01_Terrain.level23stone)

    # 24: developed/high intensity
    # 80-100 % coverage
    def L01_24(crustval, bathyval):
        return Terrain.placedeveloped(crustval, L01_Terrain.level24stone)

    # 30: bare land

    # 31: barren land
    # NB: rock/sand/clay are the documented choices!
    def L01_31(crustval, bathyval):
        return Terrain.placedesert(crustval, L01_Terrain.level31stone)

    # 32: unconsolidated shore (C-CAP data only)
    # silt/sand/gravel subject to inundation and redistribution by the water
    def L01_32(crustval, bathyval):
        return Terrain.placedesert(crustval)

    # 40: forest
    
    # 41: deciduous forest 
    # (100% redwood for us)
    def L01_41(crustval, bathyval):
        return Terrain.placeforest(crustval, 100)

    # 42: evergreen forest
    # (0% redwood for us so 100% birch)
    def L01_42(crustval, bathyval):
        return Terrain.placeforest(crustval, 0)

    # 43: mixed forest
    # (50% redwood for us so 50% birch)
    def L01_43(crustval, bathyval):
        return Terrain.placeforest(crustval, 50)

    # 50: shrubland

    # 51: dwarf shrub (Alaska only)
    def L01_51(crustval, bathyval):
        return Terrain.placeshrubland(crustval, L01_Terrain.level51stone)

    # 52: shrub/scrub
    def L01_52(crustval, bathyval):
        return Terrain.placeshrubland(crustval, L01_Terrain.level52stone)

    # 70: grassland

    # 71: grassland/herbaceous
    # NB: "grazing not tilling", so tall grass likely?
    def L01_71(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 72: sedge/herbaceous (Alaska only)
    # FIXME: phoning this in
    def L01_72(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 73: lichens (Alaska only)
    # FIXME: phoning this in
    def L01_73(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 74: moss (Alaska only)
    # FIXME: phoning this in
    def L01_74(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 80: cultivated land

    # 81: Pasture/Hay
    # like 71 eventually
    def L01_81(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 82: Cultivated crops
    # Wheat or sugar cane
    def L01_82(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 90: woody wetlands
    def L01_90(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 91: palustrine forested wetland (C-CAP only)
    def L01_91(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 92: palustrine shrub/scrub wetland (C-CAP only)
    def L01_92(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 93: estuarine forested wetland (C-CAP only)
    def L01_93(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 94: estuarine shrub/scrub wetland (C-CAP only)
    def L01_94(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 95: emergent herbaceous wetland
    def L01_95(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 96: palustrine emergent wetland
    def L01_96(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 97: estuarine emergent wetland
    def L01_97(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 98: palustrine aquatic bed
    def L01_98(crustval, bathyval):
        return Terrain.placegrass(crustval)

    # 99: estuarine aquatic bed
    def L01_99(crustval, bathyval):
        return Terrain.placegrass(crustval)

    key = 'L01'
    terdict = { 0: L01_0, 11: L01_11, 12: L01_12, 21: L01_21, 22: L01_22, 23: L01_23, 24: L01_24, 31: L01_31, 32: L01_32, 41: L01_41, 42: L01_42, 43: L01_43, 51: L01_51, 52: L01_52, 71: L01_71, 72: L01_72, 73: L01_73, 74: L01_74, 81: L01_81, 82: L01_82, 90: L01_90, 91: L01_91, 92: L01_92, 93: L01_93, 94: L01_94, 95: L01_95, 96: L01_96, 97: L01_97, 98: L01_98, 99: L01_99 }