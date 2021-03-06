#!/usr/bin/env python
"""
 ================================
| HOTPANTS Data Analysis Pipeline |
|         v1.0                   |
 ================================
| sub_cut.py |
 ==============

Summary:
        Used to cut out a region of the image you give, based on the region specified
Usage:
        python sub_make_cut.py -i input_remapping.fits -o remcut.fits -r [300:400,300:400] -v True/False
"""

from python.imclass.image import imFits
#from pyraf import iraf
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

Usage = """python sub_make_cut.py -i input_remapping.fits -o remcut.fits -r [300:400,300:400] -v True/False"""

def main(inputfits, outputfits, region, verbose):

	print "-------------"
	print "PYRAF CUTTING"
	print "-------------"

	inFits = imFits()
	inFits._Name = inputfits
	inFits._logger['Info'] = []

	copyFits = inFits.trimMyself(outname=outputfits, region=region, verbose=verbose)

	return copyFits

if __name__ == "__main__":

	# Key list for input & other constants, stupid final colon
        key_list = 'i:o:r:v:'

        # Check input
        try:
                x=sys.argv[1]
        except:
                print Usage 
                sys.exit(0)

        # Take the input & sort it out
	verbose = True
        option, remainder = getopt.getopt(sys.argv[1:], key_list)
        for opt, arg in option:
                flag = opt.replace('-','')
                
		if flag == "i":
			inputfits = arg  
		elif flag == "o":
			outputfits = arg
		elif flag == "r":
			region = arg
		elif flag == "v":
			if arg == "False":
				verbose = False
			else:
				verbose = True
		else:
			print Usage
			sys.exit(0)

	copyFits = main(inputfits, outputfits, region, verbose)
