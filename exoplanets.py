import numpy as np
import pandas as pd
import pyvo as vo
import matplotlib.pyplot as plt


def exoplanets():
    tap_service = vo.dal.TAPService("https://exoplanetarchive.ipac.caltech.edu/TAP")
    #selecting planet name, stellar effective temperature, stellar radius, and orbit semi-major axis
    #from planetary systems table
    tap_results = tap_service.search("SELECT pl_name,st_teff,st_rad,pl_orbsmax FROM ps")
    table = tap_results.to_table()
    ptable = table.to_pandas()
    #full dataframe
    print(ptable)
    size = len(ptable['st_teff'])
    temps = ptable['st_teff']
    rads = ptable['st_rad']
    orbits = ptable['pl_orbsmax']
    names = ptable['pl_name']
    cols = {'Planet Name':[],
            'Stellar Effective Temperature':[],
            'Stellar Radius':[],
            'Orbit Semi-Major Axis':[]}
    habitable = pd.DataFrame(cols)
    #caculating habitable zone for each star in dataframe
    for s in range(size):
        if np.isnan(temps[s]) or np.isnan(rads[s]) is None:
            continue
        else:
            #luminosity calculation
            lum = (rads[s]**2)*((temps[s]/5778)**4)
            #inner rhz calculation
            rhzinner = .75*(np.sqrt(lum))
            #outer rhz calculation
            rhzouter = 1.77*(np.sqrt(lum))
            #checking if planet's orbit is within the habitable zone of its star
            if rhzouter >= orbits[s] >= rhzinner:
                row = pd.DataFrame({'Planet Name':[names[s]],
                                    'Stellar Effective Temperature':[temps[s]],
                                    'Stellar Radius':[rads[s]],
                                    'Orbit Semi-Major Axis':[orbits[s]]})
                habitable = pd.concat([habitable,row])
    #dataframe containing habitable planets
    print(habitable)
    #comparing stellar and planetary aspects of habitable planets
    #stellar effective temperature vs stellar radius
    habitable.plot.scatter(x="Stellar Effective Temperature", y="Stellar Radius")
    #stellar effective temperature vs orbit semi-major axis
    habitable.plot.scatter(x="Stellar Effective Temperature",y="Orbit Semi-Major Axis")
    #stellar radius vs orbit semi-major axis
    habitable.plot.scatter(x="Stellar Radius",y="Orbit Semi-Major Axis")
    plt.show()
    return tap_results

exoplanets()
