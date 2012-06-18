#!/usr/bin/env python
"""
 ================================
| HOTPANTS Data Analysis Pipeline |
|         v1.0                   |
 ================================
| sub_mass_apphot.py |
 ==============

Summary:
        Carry out photometry on all the "best" images found using hotpants.
Usage:
        sub_mass_apphot.py -d . -b r -o object.dat

	d: directory
	b: band [g,r,i,z,J,H,K]
	o: object of interest co-ordinate file (wcs)
"""

import sys
import glob
import getopt
from sub_apphot import main as sub_apphot

__author__ = "Jonny Elliott"
__copyright__ = "Copyright 2012"
__credits__ =  "Felipe Olivares"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Jonny Elliott"
__email__ = "jonnyelliott@mpe.mpg.de"
__status__ = "Prototype"

def main(directory, bandList, objint):

	# Script outline
	#
	# 1. Find all the OBs
	# 2. Go through all the bands and run the subroutine named sub_apphot.py

	# OBs
	#
#	bandList = ['g', 'r', 'i', 'z', 'J', 'H']
	OBList = glob.glob("%s/OB*" % directory)
	for band in bandList:
		
		# temp test
		testlcx, testlcy = [], []

		# Output file
		magfile = open("%s/%s_appmag.dat" % (directory, band), "w")

		for OB in OBList:
			
			# Run sub_apphot
			time, time_err, sub_mag, sub_magerr, noise_mag, noise_magerr, subobj, noiseobj = sub_apphot(OB, band, objint)
			print "Noise mag:", noise_mag, float(noise_mag)/2.0
			if noise_magerr != "INDEF":
				sub_magerr2 = float(noise_magerr) / 2.0
			else:
				sub_magerr2 = 0

			# Write
			magfile.write("%s %s %s %s %s\n" % (OB, time, time_err, sub_mag, sub_magerr))
			
		# close file
		magfile.close()

if __name__ == "__main__":
  
        parser = OptionParser()
        parser.add_option('-d', dest='directory', help='directory of OBs', default=None)
        parser.add_option('-b', dest='band', help='band', default=None)
        parser.add_option('-o', dest='objint', help='object of interest', default=None)
        (options, args) = parser.parse_args()

        if options.directory and options.band and options.objint:
		band = options.band.split(",")
                print main(options.directory, band, options.objint)
        else:
                print __doc__
                sys.exit(0)

# Mon Dec 12 14:26:58 CET 2011
