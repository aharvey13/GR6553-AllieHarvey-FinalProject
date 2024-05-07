# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:10:42 2024

@author: Owner
"""

#This code was created with help from the Metpy SPC Convective Outlook script. I ended up incorporating hail into it
#All you have to do is add in your geojson file for hail, tor, wind, etc and change title names

import geopandas
from metpy.plots import MapPanel, PanelContainer, PlotGeometry

################################################# SPC Outlooks Maps ####################################################
################################################# Day 1 12Z Outlook ####################################################
# Read in the geoJSON file containing the convective outlook.
day1_outlook = geopandas.read_file('day1otlk_20201012_1200_cat.lyr.geojson')

###########################
# Preview the data (if you wish).
day1_outlook

###########################
# Plot the shapes from the 'geometry' column. Give the shapes their fill and stroke color by
# providing the 'fill' and 'stroke' columns. Use text from the 'LABEL' column as labels for the
# shapes.
geo = PlotGeometry()
geo.geometry = day1_outlook['geometry']
geo.fill = day1_outlook['fill']
geo.stroke = day1_outlook['stroke']
geo.labels = day1_outlook['LABEL']
geo.label_fontsize = 'large'

###########################
# Add the geometry plot to a panel and container.
panel = MapPanel()
panel.title = 'SPC Day 1 Convective Outlook (Valid 12z Oct 12 2020)'
panel.plots = [geo]
panel.area = [-120, -75, 25, 50]
panel.projection = 'lcc'
panel.layers = ['lakes', 'land', 'ocean', 'states', 'coastline', 'borders']

pc = PanelContainer()
pc.size = (12, 8)
pc.panels = [panel]
pc.show()
pc.save('SPC_Convective_12Z')

############################################## Day 1 12Z Outlook- Hail Probability ##############################################
###########################
# Read in the geoJSON file containing the convective outlook.
day1_outlook = geopandas.read_file('day1otlk_20201012_1200_hail.lyr.geojson')

###########################
# Preview the data (if you prefer).
day1_outlook

###########################
# Plot the shapes from the 'geometry' column. Give the shapes their fill and stroke color by
# providing the 'fill' and 'stroke' columns. Use text from the 'LABEL' column as labels for the
# shapes.
geo = PlotGeometry()
geo.geometry = day1_outlook['geometry']
geo.fill = day1_outlook['fill']
geo.stroke = day1_outlook['stroke']
geo.labels = day1_outlook['LABEL']
geo.label_fontsize = 'large'

###########################
# Add the geometry plot to a panel and container.
panel = MapPanel()
panel.title = 'SPC Day 1 Hail Outlook (Valid 12z Oct 12 2020)'
panel.plots = [geo]
panel.area = [-120, -75, 25, 50]
panel.projection = 'lcc'
panel.layers = ['lakes', 'land', 'ocean', 'states', 'coastline', 'borders']

pc = PanelContainer()
pc.size = (12, 8)
pc.panels = [panel]
pc.show()
pc.save('SPC_Hail_12Z')

######################################################### Day 1 1630Z Outlook #####################################################
###########################
# Read in the geoJSON file containing the convective outlook.
day1_outlook = geopandas.read_file('day1otlk_20201012_1630_cat.lyr.geojson')

###########################
# Preview the data (if you prefer).
day1_outlook

###########################
# Plot the shapes from the 'geometry' column. Give the shapes their fill and stroke color by
# providing the 'fill' and 'stroke' columns. Use text from the 'LABEL' column as labels for the
# shapes.
geo = PlotGeometry()
geo.geometry = day1_outlook['geometry']
geo.fill = day1_outlook['fill']
geo.stroke = day1_outlook['stroke']
geo.labels = day1_outlook['LABEL']
geo.label_fontsize = 'large'

###########################
# Add the geometry plot to a panel and container.
panel = MapPanel()
panel.title = 'SPC Day 1 Convective Outlook (Valid 1630Z Oct 12 2020)'
panel.plots = [geo]
panel.area = [-120, -75, 25, 50]
panel.projection = 'lcc'
panel.layers = ['lakes', 'land', 'ocean', 'states', 'coastline', 'borders']

pc = PanelContainer()
pc.size = (12, 8)
pc.panels = [panel]
pc.show()
pc.save('SPC_Convective_1630Z')

################################################# Day 1 1630Z Outlook - Hail Probability ###########################################
###########################
# Read in the geoJSON file containing the convective outlook.
day1_outlook = geopandas.read_file('day1otlk_20201012_1630_hail.lyr.geojson')

###########################
# Preview the data (if you prefer).
day1_outlook

###########################
# Plot the shapes from the 'geometry' column. Give the shapes their fill and stroke color by
# providing the 'fill' and 'stroke' columns. Use text from the 'LABEL' column as labels for the
# shapes.
geo = PlotGeometry()
geo.geometry = day1_outlook['geometry']
geo.fill = day1_outlook['fill']
geo.stroke = day1_outlook['stroke']
geo.labels = day1_outlook['LABEL']
geo.label_fontsize = 'large'

###########################
# Add the geometry plot to a panel and container.
panel = MapPanel()
panel.title = 'SPC Day 1 Hail Outlook (Valid 1630Z Oct 12 2020)'
panel.plots = [geo]
panel.area = [-120, -75, 25, 50]
panel.projection = 'lcc'
panel.layers = ['lakes', 'land', 'ocean', 'states', 'coastline', 'borders']

pc = PanelContainer()
pc.size = (12, 8)
pc.panels = [panel]
pc.show()
pc.save('SPC_Hail_1630Z')