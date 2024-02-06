import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime

#Step 1-Sort log files if they are not sorted already

##intialize the directory where you have all your vital patch  log files stored both i.e both ecg,xyz and vitals
path=''
directories=os.listdir(path)

##Incase your files aren't sorted and you want to sort them out too process them chronologically
##os.path.getmtime([direcotries])(this gets the modification times for all the files.(i.e from day 1 to day 7))
files_with_mtime = [(os.path.join(path, filename), os.path.getmtime(os.path.join(path, filename))) for filename in directories]

# List of Sorted files based on modification time(i.e from start timepoint to end timepoint[lambda is just a funtion to denote the tuple with it's index ))
files_sorted_by_mtime = sorted(files_with_mtime, key=lambda x: x[1])

#extract the sorted files
sortedfiles=[files for files,point in files_sorted_by_mtime]

##sorted signal logs(give an output list of sorted files for ecg,xyz and vitals)
ecgfiles=[file for file in sorted if file.endswith('ecg.csv') ]
vitalfiles=[file for file in sorted if file.endswith('vital.csv')  ]
xyzfiles=[file for file in sorted if file.endswith('xyz.csv')  ]





#Step 2


##A function to concatenate only ecg files of the vital patch over the whole recording period(NB:if you've got your files sorted in th the folder already)
##If you don't have your files sorted already,you can just use he preceding code to sort the files before concatenating them.

def getecgdf(path):
    directories=os.listdir(path)
    ecgdf = []
    for file in directories:   
        if file.endswith('_ecg.csv'):
           ecgpath = os.path.join(path, file)
        
           if os.path.exists(ecgpath):
              ecg = pd.read_csv(ecgpath, header=None)
              print(f'"Reading: {file}"')
              # Get amplitude and timestamp columns
              amplitudes = ecg.iloc[:, 1::2].values.flatten()
              timestamps = ecg.iloc[:, 0::2].values.flatten()
              print(f'"flattened: {file}"')
              
              if ecg.isna().any().any()==False:
                 print(f'"{file}has no missing value')
              # Create DataFrame for current file
                 df = pd.DataFrame({'Time': timestamps , 'Amplitude': amplitudes})
                 print('dataframe')
              # Append DataFrame to list
                 ecgdf.append(df)

        ecgdf_concatenated = pd.concat(ecgdf, ignore_index=True)
    
    return ecgdf_concatenated

# Concatenate all DataFrames into a single DataFrame
