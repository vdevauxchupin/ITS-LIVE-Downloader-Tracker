# ITS-LIVE Datacube Downloader & Tracker/Strains Calculator

**Hello !** This repo contains two notebooks that are allowing you to do 3 things:
- Download ITS-LIVE yearly or "daily" datacubes
- Track pixels' displacement according to their associated velocities
- Calculate strain rates for the entire datacubes

I put "daily" in quote because the proper description of these cubes is: sub-yearly.
You can have several datapoints for one day, none for months, etc... . The idea is that yearly and 
sub-yearly datacubes are stored in two different places, which makes it two different dataset.

All these operations are customizable spatially, but also temporally ! If you downloaded a yearly dataset from 1985 to 2020,
you can choose to calculate strains for the entire date range or only a few years ! Same goes for the "daily" dataset.

All the outputs generated will be saved in automatically generated folders.

***To calculate dynamic thinning/thickening:*** 
In the "Tracker_Strains" notebook, you will have the option to calculate the flux divergence.
To do that you ***NEED*** to have a glacier thickness .tif, and a .csv file with point's coordinates along the boundaries of the glacier.

There are template files in the folder Example_Qdiv, which show you how to organize your csv file (x in one column, y in the other).
Just make sure your files are in the same projection as the datacubes you are using. 

Output figures and files are stored and named based on the template:
upscale_sdate_edate

So if you run the strain for multiple upscales, the figures will be stored in the same folders but will have different names.

*Updates to come:*
I might integrate a Landsat/Sentinel image downloader which would grab the image of the AOI for which you want to track some pixels, 
ideally from the same date at which you want to start the tracking. 
However this process might add some download time to the notebook. 