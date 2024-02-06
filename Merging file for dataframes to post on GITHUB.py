# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:29:26 2024

@author: c3070014
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime

#intialize the directory where you have all your vital patch  log files stored
path='Y:/HMS Accelerometry data/Nana_PHD/VITAL PATCH DATA/'
directories=os.listdir(path)

#os.path.getmtime([direcotries])(this gets the modification times for all the files.(i.e from day 1 to day 7))
files_with_mtime = [(os.path.join(path, filename), os.path.getmtime(os.path.join(path, filename))) for filename in directories]

# List of Sorted files based on modification time(i.e from start timepoint to end timepoint[lambda is just a funtion to denote the tuple ))
files_sorted_by_mtime = sorted(files_with_mtime, key=lambda x: x[1])

#get only the files sorted in the sorted files and epochs dictionary
sortedfiles=[files for files,point in files_sorted_by_mtime]

#sorted signal logs
ecgfiles=[file for file in sorted if file.endswith('ecg.csv') ]
vitalfiles=[file for file in sorted if file.endswith('vital.csv')  ]
xyzfiles=[file for file in sorted if file.endswith('xyz.csv')  ]




#ecg1=pd.read_csv('Y:/HMS Accelerometry data/Nana_PHD/VITAL PATCH DATA/1702485393033_VC2B008BF_052AE4_ecg.csv',header=None)
#amp=ecg1.iloc[:,1::2].values
#timestamp=ecg1.iloc[:,0::2].values
#amp[0,0]
#o=pd.Series(amp)
#flatten the array to one line
#flattened_array = amp.flatten()
#convert to series
#col1series=pd.Series(amp.flatten())
#timeseries=pd.Series(timestamp.flatten())
#pd.concat([col1series,timeseries],axis=1)
#Z=pd.DataFrame({'amp':col1series,'t':timeseries})

# getting ecg dataframe for all ecg files

def getecgdf(ecgfiles):
    
    ecgdf = []
    for file in ecgfiles:   
        ecgpath = os.path.join(path, file)
        if os.path.exists(ecgpath):
           ecg = pd.read_csv(ecgpath, header=None)
           print(f'"first file{file}"')
           # Get amplitude and timestamp columns
           amplitudes = ecg.iloc[:, 1::2].values
           timestamps = ecg.iloc[:, 0::2].values

           # Flatten amplitude and timestamp arrays
           flattened_amplitudes = amplitudes.flatten()
           flattened_timestamps = timestamps.flatten()
           print('flattened')
          # Create DataFrame for current file
           df = pd.DataFrame({'Time': flattened_timestamps, 'Amplitude': flattened_amplitudes})
           print('dataframe')
          # Append DataFrame to list
           ecgdf.append(df)

# Concatenate all DataFrames into a single DataFrame
#ecgdf_concatenated = pd.concat(ecgdf, ignore_index=True)












# getting vitals dataframe






# gettting  xyz activity dataframe

