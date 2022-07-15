# Habitable-Exoplanets-Project
Utilization of NASA Exoplanet API and Archive to determine habitability of confirmed exoplanets:

Accessed TAP service for cofirmed planets via the NASA Exoplanet Archive. Searched and selected planet name (pl_name), stellar effective temperature (st_teff) in K, stellar radius (st_rad) in terms of solar radii, and planetary orbit semi-major axis (pl_orbsmax) in AU columns from the Planetary System table. Converted the VOtable to Pandas Dataframe. Used data from dataframe to calculate habitable zone of each star and determine if each planet orbits within the star's habitable zone. Proceeded to plot data from habitable planets to see if there were any patterns that appear in habitable planets. 

Through the plots it is shown that the Stellar Effective Temperature is variable across many of the habitable planets whereas, the Orbit Semi-Major Axis is bunched mostly between 0 and 1.5AU then becomes increasingly sparse as the orbit increases. Similarly most of the habitable planets orbit stars with a Stellar Radius between 0 and 2 solar radii and again become increasingly sparse as the radius increases.
