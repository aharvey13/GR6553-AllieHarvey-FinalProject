# GR6553-AllieHarvey-FinalProject

Welcome to my Final Project!

Here you will find data and scripts relating to different parameters, surface analysis, SPC outlooks, and radar data
- Each has a separate folder (excluding radar data/scan png/gif)

#How to Pull Data: 

Acquiring Model Data:
- Since the model data is too big to be put in separately, here is how to pull it:
- First, I went online and searched "AWS HRRR data".
- There, I went to Amazon Web Services (AWS) and went to the third link (aws bucket).
- Then, go to hrrrzarr -> sfc -> year/month/day. (Here is the link I used: https://hrrrzarr.s3.amazonaws.com/index.html#sfc/)
- At this point, you will be able to download your data (I used anl version)

Acquiring WPC Data:
- For WPC analysis, I had to create my own textfile using information from the Iowa Environmental Mesonet for a certain hour since the textfile includes data from all forecast hours for a certain day.
- Here is the link for pulling different days - it is under National Weather Service Raw Text Product: https://www.mesonet.agron.iastate.edu/wx/afos/p.php?pil=CODSUS&e=202010201500

Acquiring Radar Data:
- I pulled radar data from Amazon Web Services (AWS). Here is the link: https://s3.amazonaws.com/noaa-nexrad-level2/index.html
- Once the link is pulled, go to the year -> month -> date -> station id and then download the data (each scan is separate)
- I did not include MDM for any of my radar plots
- For my radar loop, I used a gif generator on Google
  
Acquiring SPC Data:
- I pulled archive data from the SPC website - here is the link: https://www.spc.noaa.gov/archive/
- Under archive convective outlooks, put the dates of when you want to start and end the data
- Then download the time and product you need (I used .geojson in my code)

##Python Script Credit:

- Surface Analysis: Metpy
- SPC Convective Analysis: Metpy
- Radar: Code given in class
- Sounding: Combination of simple and advanced sounding from Metpy
- Parameters: Materials/code given in class

###Breaking Down the Data:

- Each Python script under the Python Script folder has detailed comments (either from me or Metpy) on how to go through each script.
- Some comments include reasonings for changes and extra details needed to understand the code
