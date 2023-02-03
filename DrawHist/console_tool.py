#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:52:21 2022

@author: clement
"""

import sys
import os
import argparse
from .DrawHist_script import DrawHistFromCSV

def path(string):
    if os.path.exists(string):
        return string
    else:
        sys.exit(f'File not found: {string}')


def console_tool():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputCSV', metavar='inputcsv', type=path, help='Path to input csv (str), containing as first column paths to images, as second paths to ROI, and as third colors.', required=True)
    parser.add_argument('--min', metavar='min', type=int, help='Minimum value to consider for histograms and statistics (int).', required=True)
    parser.add_argument('--max', metavar='max', type=int, help='Maximum value to consider for histograms and statistics (int).', required=True)
    parser.add_argument('--outfolder', metavar='outfolder', type=str, help='Path to the folder where results will be saved (str).', required=True)

    
    parse_args, unknown = parser.parse_known_args()
    if not parse_args.inputcsv[-7:] == '.csv':
        raise IOError('Input file must be of type .csv')

    os.makedirs(parse_args.outfolder, exist_ok=True)
    DrawHistFromCSV(parse_args.inputcsv, parse_args.min, parse_args.max, parse_args.outfolder)


