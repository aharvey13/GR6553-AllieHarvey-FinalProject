# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 19:30:02 2024

@author: Owner
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy.feature as cf
import cartopy.crs as ccrs
import pygrib

##################################### 17Z Weather Parameters ###############################
grbHRRR = pygrib.open ('hrrr.t17z.wrfprsf00.grib2')

############################### 500 mb Heights/Relative Humidity/Temp ########################
#Step 1: What are we contouring (ie:fields)
grbHRRR.select(name='Temperature')
grbHRRR.select(name='Geopotential height')
grbHRRR.select(name='Relative humidity')

#Step 2:Pulling in data for certain heights
temp500 = grbHRRR[254]; temp = temp500['values']
geopot500 = grbHRRR[253]; geopot = geopot500['values']
relhumidity500 = grbHRRR[255]; relhumidity = relhumidity500['values']
lats, lons = temp500.latlons()

#Step 3: Setting up the cartopy map
fig = plt.figure (figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-120.,-72.,22.,51.])
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='gray')
ax.add_feature(cf.STATES,edgecolor='gray')
ax.add_feature(cf.BORDERS,edgecolor='gray',linestyle='-')
ax.add_feature(cf.LAKES,color='lightsteelblue',alpha=0.5)

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='white', alpha=0.5, linestyle='--')

gl.top_labels = False
gl.left_labels = False

#Step 4: Plotting the data
map1=plt.contourf(lons,lats,relhumidity,np.arange(40,101,10), cmap=plt.cm.YlGn,transform=ccrs.PlateCarree())

cbar = plt.colorbar (location='bottom')
cbar.set_label ('percent')

c=plt.contour (lons, lats, temp-273, np.arange(np.min(temp-273),np.max(temp-273),4), linewidths=2, linestyles=':', cmap=plt.cm.cool_r,transform=ccrs.PlateCarree())
cs=plt.contour (lons,lats,geopot/10,np.arange(np.min(geopot/10),np.max(geopot/10),6), linestyles='solid', linewidths=2, colors='black', transform=ccrs.PlateCarree())
plt.title ('500 mb Heights (dm) / Temperature (C) / Humidity (%)\n17Z Oct 12th 2020')
plt.show()
#plt.savefig('500 mb 17Z - US')
plt.close()

############################## 500 mb Heights/Relative Humidity/Temp (Zoomed in on Chicago Metro Area) ####################################
grbHRRR = pygrib.open ('hrrr.t17z.wrfprsf00.grib2')


#Step 1: What are we contouring (ie:fields)
grbHRRR.select(name='Temperature')
grbHRRR.select(name='Geopotential height')
grbHRRR.select(name='Relative humidity')

#Step 2:Pulling in data for certain heights
temp500 = grbHRRR[254]; temp = temp500['values']
geopot500 = grbHRRR[253]; geopot = geopot500['values']
relhumidity500 = grbHRRR[255]; relhumidity = relhumidity500['values']
lats, lons = temp500.latlons()

#Step 3: Setting up the cartopy map
fig = plt.figure (figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-90.,-85.,40.,45.]) #Map extent for the Chicago Metro Area
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='gray')
ax.add_feature(cf.STATES,edgecolor='gray')
ax.add_feature(cf.BORDERS,edgecolor='gray',linestyle='-')
ax.add_feature(cf.LAKES,color='lightsteelblue',alpha=0.25)

#Step 4: Plotting the data
map1=plt.contourf(lons,lats,relhumidity,np.arange(0,101,10), cmap=plt.cm.YlGn,transform=ccrs.PlateCarree())

cbar = plt.colorbar (location='bottom')
cbar.set_label ('percent')

c=plt.contour (lons, lats, temp-273, np.arange(np.min(temp-273),np.max(temp-273),4), linewidths=2, linestyles=':', cmap=plt.cm.cool_r,transform=ccrs.PlateCarree())
cs=plt.contour (lons,lats,geopot/10,np.arange(np.min(geopot/10),np.max(geopot/10),6), linestyles='solid', linewidths=2, colors='black', transform=ccrs.PlateCarree())
plt.title ('500 mb Heights (dm) / Temperature (C) / Humidity (%)\n17Z Oct 12th 2020')
plt.show()
#plt.savefig('500 mb 17Z - Chicago Area')
plt.close()

#################################### 500mb Vertical Velocities (Zoomed in on Chicago Metro Area) #####################################3
################## Disclaimer: Vertical Velocities map did not plot correctly - did not include this in my final project but I am leaving it here anyways #####################################
grbHRRR = pygrib.open ('hrrr.t17z.wrfprsf00.grib2')


#Step 1: What are we contouring (ie:fields)
grbHRRR.select(name='Vertical velocity')
grbHRRR.select(name='U component of wind')
grbHRRR.select(name='V component of wind')

#Step 2:Pulling in data for certain heights
vertvelo500 = grbHRRR[258]; verticalvelocity = vertvelo500['values']
uwnd500 = grbHRRR[259]; uwnd = uwnd500['values']
vwnd500 = grbHRRR[260]; vwnd = uwnd500['values']
lats, lons = vertvelo500.latlons()

#Step 3: Setting up the cartopy map
fig = plt.figure (figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-90.,-85.,40.,45.]) #Map extent for the Chicago Metro Area
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='gray')
ax.add_feature(cf.STATES,edgecolor='gray')
ax.add_feature(cf.BORDERS,edgecolor='gray',linestyle='-')
ax.add_feature(cf.LAKES,color='lightsteelblue',alpha=0.25)

#Step 4: Plotting the data
map3=plt.contourf(lons,lats,verticalvelocity,np.arange(-60,40,10),cmap=plt.cm.hot_r,transform=ccrs.PlateCarree())
cbar = plt.colorbar (location='bottom')
cbar.set_label ('Pa s^-1')

plt.barbs(lons[::50,::50],lats[::50,::50],uwnd[::50,::50],vwnd[::50,::50],transform=ccrs.PlateCarree())
plt.title ('500mb Vertical Velocities (Pa s^-1)/ Isotachs (knots)\n17Z Oct 12th 2020')
plt.show()
#plt.savefig('500 mb 17Z -VV')
plt.close()

######################################## Severe Parameters - SRH (Zoomed in on Chicago Metro Area) ########################################
grbHRRR = pygrib.open ('hrrr.t17z.wrfprsf00.grib2')


#Step 1: What are we contouring (ie:fields)
grbHRRR.select(name='Storm relative helicity')

#Step 2:Pulling in data for certain heights
srh = grbHRRR[665]; srh0to3 = srh['values']
lats, lons = srh.latlons()

#Step 3: Setting up the cartopy map
fig = plt.figure (figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-90.,-85.,40.,45.]) #Map extent for the Chicago Metro Area
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='black')
ax.add_feature(cf.STATES,edgecolor='black')
ax.add_feature(cf.BORDERS,edgecolor='black',linestyle='-')
ax.add_feature(cf.LAKES,color='lightsteelblue',alpha=0.25)

#Step 4: Plotting the data
map4=plt.contourf(lons,lats,srh0to3,np.arange(0,400,25), cmap=plt.cm.plasma_r,transform=ccrs.PlateCarree())

cbar = plt.colorbar (location='bottom')
cbar.set_label ('m^2 s^-2')

plt.title ('0-3km Storm Relative Helicity (m^2 s^-2)\n 17Z Oct 12th 2020', fontsize=15)
plt.show()
#plt.savefig('SRH 17Z')
plt.close()

######################################## Severe Parameters - MUCAPE (Zoomed in on Chicago Metro Area) ########################################
grbHRRR = pygrib.open ('hrrr.t17z.wrfprsf00.grib2')


#Step 1: What are we contouring (ie:fields)
grbHRRR.select(name='Convective available potential energy')

#Step 2:Pulling in data for certain heights
CAPE = grbHRRR[688]; CAPEMU = CAPE['values']
lats, lons = CAPE.latlons()

#Step 3: Setting up the cartopy map
fig = plt.figure (figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-90.,-85.,40.,45.]) #Map extent for the Chicago Metro Area
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='black')
ax.add_feature(cf.STATES,edgecolor='black')
ax.add_feature(cf.BORDERS,edgecolor='black',linestyle='-')
ax.add_feature(cf.LAKES,color='lightsteelblue',alpha=0.25)

#Step 4: Plotting the data
map5=plt.contourf(lons,lats,CAPEMU,np.arange(0,500,25), cmap=plt.cm.viridis_r,transform=ccrs.PlateCarree())

cbar = plt.colorbar (location='bottom')
cbar.set_label ('J kg^-1')

plt.title ('Convective Available Potential Energy (J kg^-1)\n 17Z Oct 12th 2020', fontsize=15)
plt.show()
#plt.savefig('CAPE 17Z')
plt.close()


##################################### 20Z Weather Parameters ###############################
grbHRRR = pygrib.open ('hrrr.t20z.wrfprsf00.grib2')

############################### 500 mb Heights/Relative Humidity/Temp ########################
#Step 1: What are we contouring (ie:fields)
grbHRRR.select(name='Temperature')
grbHRRR.select(name='Geopotential height')
grbHRRR.select(name='Relative humidity')

#Step 2:Pulling in data for certain heights
temp500 = grbHRRR[254]; temp = temp500['values']
geopot500 = grbHRRR[253]; geopot = geopot500['values']
relhumidity500 = grbHRRR[255]; relhumidity = relhumidity500['values']
lats, lons = temp500.latlons()

#Step 3: Setting up the cartopy map
fig = plt.figure (figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-120.,-72.,22.,51.])
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='gray')
ax.add_feature(cf.STATES,edgecolor='gray')
ax.add_feature(cf.BORDERS,edgecolor='gray',linestyle='-')
ax.add_feature(cf.LAKES,color='lightsteelblue',alpha=0.5)

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='white', alpha=0.5, linestyle='--')

gl.top_labels = False
gl.left_labels = False

#Step 4: Plotting the data
map6=plt.contourf(lons,lats,relhumidity,np.arange(40,101,10), cmap=plt.cm.YlGn,transform=ccrs.PlateCarree())

cbar = plt.colorbar (location='bottom')
cbar.set_label ('percent')

c=plt.contour (lons, lats, temp-273, np.arange(np.min(temp-273),np.max(temp-273),4), linewidths=2, linestyles=':', cmap=plt.cm.cool_r,transform=ccrs.PlateCarree())
cs=plt.contour (lons,lats,geopot/10,np.arange(np.min(geopot/10),np.max(geopot/10),6), linestyles='solid', linewidths=2, colors='black', transform=ccrs.PlateCarree())
plt.title ('500 mb Heights (dm) / Temperature (C) / Humidity (%)\n20Z Oct 12th 2020')
plt.show()
#plt.savefig('500 mb 20Z')
plt.close()

############################## 500 mb Heights/Relative Humidity/Temp (Zoomed in on Chicago Metro Area) ####################################
grbHRRR = pygrib.open ('hrrr.t20z.wrfprsf00.grib2')

#Step 1: What are we contouring (ie:fields)
grbHRRR.select(name='Temperature')
grbHRRR.select(name='Geopotential height')
grbHRRR.select(name='Relative humidity')

#Step 2:Pulling in data for certain heights
temp500 = grbHRRR[254]; temp = temp500['values']
geopot500 = grbHRRR[253]; geopot = geopot500['values']
relhumidity500 = grbHRRR[255]; relhumidity = relhumidity500['values']
lats, lons = temp500.latlons()

#Step 3: Setting up the cartopy map
fig = plt.figure (figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-90.,-85.,40.,45.]) #Map extent for the Chicago Metro Area
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='gray')
ax.add_feature(cf.STATES,edgecolor='gray')
ax.add_feature(cf.BORDERS,edgecolor='gray',linestyle='-')
ax.add_feature(cf.LAKES,color='lightsteelblue',alpha=0.25)

#Step 4: Plotting the data
map7=plt.contourf(lons,lats,relhumidity,np.arange(0,101,10), cmap=plt.cm.YlGn,transform=ccrs.PlateCarree())

cbar = plt.colorbar (location='bottom')
cbar.set_label ('percent')

c=plt.contour (lons, lats, temp-273, np.arange(np.min(temp-273),np.max(temp-273),4), linewidths=2, linestyles=':', cmap=plt.cm.cool_r,transform=ccrs.PlateCarree())
cs=plt.contour (lons,lats,geopot/10,np.arange(np.min(geopot/10),np.max(geopot/10),6), linestyles='solid', linewidths=2, colors='black', transform=ccrs.PlateCarree())
plt.title ('500 mb Heights (dm) / Temperature (C) / Humidity (%)\n20Z Oct 12th 2020')
plt.show()
#plt.savefig('500 mb 20Z - Chicago Area')
plt.close()

######################################## Severe Parameters - SRH (Zoomed in on Chicago Metro Area) ########################################
grbHRRR = pygrib.open ('hrrr.t20z.wrfprsf00.grib2')

#Step 1: What are we contouring (ie:fields)
grbHRRR.select(name='Storm relative helicity')

#Step 2:Pulling in data for certain heights
srh = grbHRRR[665]; srh0to3 = srh['values']
lats, lons = srh.latlons()

#Step 3: Setting up the cartopy map
fig = plt.figure (figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-90.,-85.,40.,45.]) #Map extent for the Chicago Metro Area
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='black')
ax.add_feature(cf.STATES,edgecolor='black')
ax.add_feature(cf.BORDERS,edgecolor='black',linestyle='-')
ax.add_feature(cf.LAKES,color='lightsteelblue',alpha=0.25)

#Step 4: Plotting the data
map8=plt.contourf(lons,lats,srh0to3,np.arange(0,400,25), cmap=plt.cm.plasma_r,transform=ccrs.PlateCarree())

cbar = plt.colorbar (location='bottom')
cbar.set_label ('m^2 s^-2')

plt.title ('0-3km Storm Relative Helicity (m^2 s^-2)\n 20Z Oct 12th 2020', fontsize=15)
plt.show()
#plt.savefig('SRH 20Z')
plt.close()

######################################## Severe Parameters - MUCAPE (Zoomed in on Chicago Metro Area) ########################################
grbHRRR = pygrib.open ('hrrr.t20z.wrfprsf00.grib2')

#Step 1: What are we contouring (ie:fields)
grbHRRR.select(name='Convective available potential energy')

#Step 2:Pulling in data for certain heights
CAPE = grbHRRR[688]; CAPEMU = CAPE['values']
lats, lons = CAPE.latlons()

#Step 3: Setting up the cartopy map
fig = plt.figure (figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

ax.set_extent([-90.,-85.,40.,45.]) #Map extent for the Chicago Metro Area
ax.add_feature(cf.LAND,color='wheat')
ax.add_feature(cf.OCEAN,color='lightsteelblue')
ax.add_feature(cf.COASTLINE,edgecolor='black')
ax.add_feature(cf.STATES,edgecolor='black')
ax.add_feature(cf.BORDERS,edgecolor='black',linestyle='-')
ax.add_feature(cf.LAKES,color='lightsteelblue',alpha=0.25)
#For this parameter, I took gridlines off in order to see the SRH colors better

#Step 4: Plotting the data
map9=plt.contourf(lons,lats,CAPEMU,np.arange(0,1000,100), cmap=plt.cm.viridis_r,transform=ccrs.PlateCarree())

cbar = plt.colorbar (location='bottom')
cbar.set_label ('J kg^-1')

plt.title ('Convective Available Potential Energy (J kg^-1)\n 20Z Oct 12th 2020', fontsize=15)
plt.show()
#plt.savefig('CAPE 20Z')
plt.close()