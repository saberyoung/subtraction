#!/usr/bin/env python
"""
 ================================
| HOTPANTS Data Analysis Pipeline |
|         v1.0                   |
 ================================
| sub_check_pants.py |
 ==============

Summary:
        
Usage:
       python sub_check_pants.py -d dir
"""

import python.subtraction.sub_mass_pypants as bypants
import python.subtraction.wcsremap as remap
import os, re, glob, sys, getopt

__author__ = "Jonny Elliott"
__copyright__ = "Copyright 2012"
__credits__ =  "Felipe Olivares"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Jonny Elliott"
__email__ = "jonnyelliott@mpe.mpg.de"
__status__ = "Prototype"

def main(directory):

	print "#############"
	print "PYPANTS CHECK"
	print "#############"

	logger = {}
	logger['Info'] = []

	# Bands
	bandList = ["g", "r", "i", "z", "J", "H", "K"]

	# OB in the remapping folder
	OBList = glob.glob("%s/OB*" % directory)
	ParLen = bypants.parameters()
	ParLen = len(ParLen)

	# Inform user
	print "OB Mapping Information"
	print "######################"
	print "Number of OBs: %f" % len(OBList)
	print "OBs: %s" % OBList
	print "######################"
	print ""
	print "Individual OB information"
	print "#########################"

	# Check each folder
	Missing_list = []
	missing = 0

	for OB in OBList:
		band_inc = 0
		for band in bandList:
			sub_path = "%s/%s/sub" % (OB, band)
			cube_path = "%s/cube_*" % (sub_path)

			if not os.path.exists(sub_path):
				missing = missing + ParLen
			
			cubeList = glob.glob(cube_path)
			for cube in cubeList:
				
				if not os.path.exists("%s/diff_g.fits" % (cube)):

					#print "!!!MISSING CUBE!!!"
					#print "OB: %s" % (OB)
					#print "Band: %s" % (band)
					#print "Cube: %s" % (cube)
					Missing_list.append([OB, band, cube])
					missing = missing+1
					#print ""
	
		print "OB: %s" % OB	
		print "Total missing: %d/%d" % (missing, len(bandList)*ParLen)
		missing = 0


	if len(Missing_list)<10:
		print "Final missing list:"
		for missing in Missing_list:
			print "OB: %s, band: %s, cube: %s" % (missing[0], missing[1], missing[2])

	else:
		print "Nothing missing"


	print "Total missing: %d/%d" % (len(Missing_list), len(OBList)*len(bandList)*len(cubeList))
	
	return(Missing_list)

if __name__ == "__main__":

	# Key list for input & other constants, stupid final colon
        key_list = 'd:'

        # Check input
        try:
                x=sys.argv[1]
        except:
                print __doc__
                sys.exit(0)

        # Take the input & sort it out
        option, remainder = getopt.getopt(sys.argv[1:], key_list)
        for opt, arg in option:
                flag = opt.replace('-','')
                
		if flag == "d":
			directory = arg  
		else:
			print __doc__
			sys.exit(0)

	Missing_list = main(directory)
