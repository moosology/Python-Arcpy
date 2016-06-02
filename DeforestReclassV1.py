###############################################################################
#
# Author: Christian Snelgrove
# Purpose: Reclassifies rasters that are classified in a daily format, meaning
# their values range from 1-365 (or 366) corresponding to the day of the year. 
# This script accounts for leap year differences and can be used to reclassify
# rasters that are part of leap years and ones that are not.
# Created: 2/9/2016  
# Last Edited: 6/1/2016
#
###############################################################################

# Imports arcpy, os. and checks out the Spatial Analyst extension. 
import arcpy
arcpy.CheckOutExtension("Spatial")
import os

# Prompts user for workspace input.
print "Please input where your rasters are located"
wksp = raw_input(">")

# Replaces back slashes in path with forward slashes, as black slashes do not 
# work without either an escape sequence or an r before the path name.
wksp = wksp.replace("\\", "/")

# Sets the workspace. 
arcpy.env.workspace = wksp

# Create empty lists that rasters can be sorted into later. 
leap_rasters = []
non_leap_rasters = []

# Lists rasters found in workspace
rasters = arcpy.ListRasters()

# Open a for-loop to sort rasters into lists based on whether or not they come 
# from a leap year.
for raster in rasters:
    
    #Takes input from user with regards to what year each raster is from
    print "Year of", raster
    year = int(raw_input(">"))
    
    # Sorts each raster into its proper list based on whether or not it is a
    # leap year. Note that only leap years are divisible by 4 with no remainder.
    # This makes the modulus function suitable for this purpose. 
    if (year % 4) == 0:
        leap_rasters.append(raster)
    elif (year % 4) != 0:
        non_leap_rasters.append(raster)
    else:
        pass
    
print "All rasters are sorted. Reclassifying them now..."

# Initiates for loop to reclassify sorted rasters into monthly values. 
for raster in leap_rasters:
    outReclass1 = arcpy.sa.Reclassify(raster, "Value", arcpy.sa.RemapRange(
                                                    [[1, 31, 1], [31, 60, 2],
                                                    [60, 91, 3], [91, 121, 4],
                                                    [121, 152, 5], [152, 182, 6],
                                                    [182, 213, 7], [213, 244, 8],
                                                    [244, 274, 9], [274, 305, 10],
                                                    [305, 335, 11], [335, 366, 12]]))
                                                    
    outReclass1.save(arcpy.env.workspace + os.sep + raster + "_monthly")
    
print "Leap year rasters finished!"

# Initiates for loop to reclassify sorted rasters into monthly values.     
for raster in non_leap_rasters:
    outReclass2 = arcpy.sa.Reclassify(raster, "Value", arcpy.sa.RemapRange(
                                                    [[1, 31, 1], [31, 59, 2],
                                                    [59, 90, 3], [90, 120, 4],
                                                    [120, 151, 5], [151, 181, 6],
                                                    [181, 212, 7], [212, 243, 8],
                                                    [243, 273, 9], [273, 304, 10],
                                                    [304, 334, 11], [334, 365, 12]]))
                                                    
    outReclass2.save(arcpy.env.workspace + os.sep + raster + "_monthly")
    
print "Non-leap year rasters finished!"
    
print "Work complete!" 