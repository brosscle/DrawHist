#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:03:33 2023

@author: clement
"""
import os
import numpy as np
import nibabel as nib
import nibabel.processing
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.stats import t

def DrawHist(list_images, list_rois, list_colors, min_val, max_val, outfolder):
    plt.figure()
    BigVec = []
    uni_col = list(np.unique(list_colors))
    for i in range(len(uni_col)):
        BigVec.append([])
    
    
    td = datetime.now()
    df_string = td.strftime("%H_%M_%S")
    
    
    
    for im, roi, col in zip(list_images, list_rois, list_colors):
        print(im)
        print(roi)
        print(col)
        im_h = nib.load(im)
        seg_h = nib.load(roi)

        # if im_h.shape != seg_h.shape:
        #     print('seg_shape : ')
        #     print(seg_h.shape)
        #     print('CT_shape : ')
        #     print(im_h.shape)
        #     print('RESAMPLING file '+roi)
        #     seg_resampled = nibabel.processing.resample_from_to(seg_h, im_h, order = 0)
        #     splt = roi.split('.')
        #     splt[-3] = splt[-3]+'_QuickResample'
        #     new_path_image = '.'.join(splt)
        #     nib.save(seg_resampled, new_path_image)
        #     roi = new_path_image
        #     seg_h = nib.load(roi)
    
    
        im_vol = im_h.get_fdata()
        seg = seg_h.get_fdata()
    
        seg_bin = seg>0
        
        Vec = im_vol[seg_bin]
        BigVec[uni_col.index(col)] = np.concatenate((BigVec[uni_col.index(col)], Vec))        
        res = plt.hist(Vec, range=(min_val, max_val), bins=max_val-min_val, color = col, density=True, alpha=0.5)
    
    splt = im.split(os.sep)
    basename = splt[-1]
    splt2 = basename.split('.')
    basename2 = splt2[0]
    plt.title(basename2)
    fname = outfolder+os.sep + basename2 + '_' + df_string + '.png'
    plt.savefig(fname, dpi='figure')
    plt.close()
    
    
    outfile = outfolder+ os.sep + basename2 + '_' + df_string + '.csv'
    with open(outfile, 'w', newline='') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        Def = ['Color', 'number_images', 'number_voxels', 'mean', 'std', 'median', 'percentile5', 'percentile95', 'confidence_interval_95_low', 'confidence_interval_95_high']
        wr.writerow(Def)
        for ind, vecval in enumerate(BigVec):
            
            val_min = vecval<max_val
            val_max = vecval>min_val
            val_to_keep = val_min & val_max
            vecval_bis = vecval[val_to_keep]
            n = len(vecval_bis)
            mean = np.mean(vecval_bis)
            std = np.std(vecval_bis)
            med = np.median(vecval_bis)
            per5 = np.percentile(vecval_bis, 5)
            per95 = np.percentile(vecval_bis, 95)
        
            confidence = 0.95
            dof = n-1
            t_crit = np.abs(t.ppf((1-confidence)/2,dof))
            conf_int_low = mean-std*t_crit/np.sqrt(n)
            conf_int_high = mean+std*t_crit/np.sqrt(n)
            
    
            stat = [uni_col[ind], list_colors.count(uni_col[ind]), n, mean, std, med, per5, per95, conf_int_low, conf_int_high]
            wr.writerow(stat)



def DrawHistFromCSV(csvfilepath, min_val, max_val, outfolder):
    with open(csvfilepath, 'r', newline='') as csvfile:
        D = csv.reader(csvfile)
        ims = []
        rois = []
        colors = []
        for row in D:
            ims.append(row[0])
            rois.append(row[1])
            colors.append(row[2])
            
    DrawHist(ims, rois, colors, min_val, max_val, outfolder)
    



# mi = 6
# ma = 140
# outf = '/Users/clement/Desktop/test_histo/'


# incsv = '/Users/clement/Desktop/test_histo/InData.csv'

# DrawHistFromCSV(incsv, mi, ma, outf)

