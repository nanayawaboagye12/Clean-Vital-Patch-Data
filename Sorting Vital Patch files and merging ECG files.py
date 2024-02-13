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
##If you don't have your files sorted already,you can just use the above code to sort the files before concatenating them.

def getecgdf(path):
    # path=''
    directories=os.listdir(path)
    ecgdf = []
    for file in directories:   
        if file.endswith('_ecg.csv'):
           ecgpath = os.path.join(path, file)
        
           if os.path.exists(ecgpath):
              ecg = pd.read_csv(ecgpath, header=None)
              print(f'"first file{file}"')
              # Get amplitude and timestamp columns
              amplitudes = ecg.iloc[:, 1::2].values.flatten()
              timestamps = ecg.iloc[:, 0::2].values.flatten()
              print('flattened')
              
              if ecg.isna().any().any()==False:
              # Create DataFrame for current file
                 df = pd.DataFrame({'Time': timestamps , 'Amplitude': amplitudes})
                 print('dataframe')
              # Append DataFrame to list
                 ecgdf.append(df)

           ecgdf_concatenated = pd.concat(ecgdf, ignore_index=True)
        
   ##operations on the epoch
    Time=ecgdf_concatenated['Time'].values
    files_sorted_by_mtime = sorted(Time)
    slicedtime=[(str(times))[:-3] for times in Time]
    slicedtime=[(int(times)) for times in slicedtime]
    timesinseconds=pd.to_datetime(slicedtime,unit='s')
    ecgdf_concatenated['New Time']=timesinseconds
    #sort time
    ecgdf_concatenated.set_index('New Time', inplace=True)
    # Sort DataFrame by index (epochs)
    ecgdf_concatenated.sort_index(inplace=True)
        
    if len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1])) == 5:
        print('The length of recording is 5 days,concatenated files for 5 days')

    elif len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1])) == 6:
        print('The length of recording is 6 days,concatenating files for 6 days')
                         
    elif len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1])) == 7:
        print('The length of recording is 7 days,concatenating files for 7 days')    

    elif len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1])) <= 4:
        print(f'"The length of recording is {len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1]))},concatenating files for {len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1]))} days  "')
    
    return ecgdf_concatenated




# getting vitals dataframe
def getvitaldf(path):
    # path=''
    directories=os.listdir(path)
    vitaldf = []
    for file in directories:   
        if file.endswith('_vitals.csv'):
           vitalpath = os.path.join(path, file)
        
           if os.path.exists(vitalpath):
              ecg = pd.read_csv(vitalpath, header=None)
              print(f'"first file{file}"')
              # Get amplitude and timestamp columns
              Posture = ecg.iloc[:,5].values.flatten()
              Steps = ecg.iloc[:,4].values.flatten()
              Temperature= ecg.iloc[:,3].values.flatten()
              Respirationrate = ecg.iloc[:,2].values.flatten()
              RRinterval = ecg.iloc[:,6].values.flatten()
              Heartrate = ecg.iloc[:,1 ].values.flatten()
              timestamps = ecg.iloc[:,0].values.flatten()
              print('flattened')
              
              if ecg.isna().any().any()==True:
              # Create DataFrame for current file
                 # Time=ecg[0].values
                 # files_sorted_by_mtime = sorted(Time)
                 # slicedtime=[(str(times))[:-3] for times in Time]
                 # slicedtime=[(int(times)) for times in slicedtime]
                 # timesinseconds=pd.to_datetime(slicedtime,unit='s')   
                 df = pd.DataFrame({'Time': timestamps , 'Heart Rate':Heartrate ,'Respiration Rate':Respirationrate,'Temperature':Temperature,'Stepscount':Steps,'Posture':Posture,'R-R Interval':RRinterval})
                 print('dataframe')
              # Append DataFrame to list
                 vitaldf.append(df)
                 
    vitaldf_concatenated = pd.concat(vitaldf, ignore_index=True)
    
    
    Time=vitaldf_concatenated['Time'].values
    files_sorted_by_mtime = sorted(Time)
    slicedtime=[(str(times))[:-3] for times in Time]
    slicedtime=[(int(times)) for times in slicedtime]
    timesinseconds=pd.to_datetime(slicedtime,unit='s')
    vitaldf_concatenated['New Time']=timesinseconds
    #sort time
    vitaldf_concatenated.set_index('New Time', inplace=True)
    # Sort DataFrame by index (epochs)
    vitaldf_concatenated.sort_index(inplace=True)

           
    if len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1])) == 5:
       print('The length of recording is 5 days,concatenated files for 5 days')

    elif len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1])) == 6:
         print('The length of recording is 6 days,concatenating files for 6 days')
                     
    elif len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1])) == 7:
         print('The length of recording is 7 days,concatenating files for 7 days')    

    elif len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1])) <= 4:
         print(f'"The length of recording is {len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1]))},concatenating files for {len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1]))} days  "')
    
    return vitaldf_concatenated





#getxyzfiles

def getxyzdf(path):
    # path=''
    directories=os.listdir(path)
    xyzdf = []
    for file in directories:   
        if file.endswith('xyz.csv'):
           xyzpath = os.path.join(path, file)
        
           if os.path.exists(xyzpath):
              xyz = pd.read_csv(xyzpath, header=None)
              print(f'"first file{file}"')
              # Get amplitude and timestamp columns
              z = xyz.iloc[:,3].values.flatten()
              y = xyz.iloc[:,2].values.flatten()
              
              x = xyz.iloc[:, 1].values.flatten()
              timestamps = xyz.iloc[:, 0].values.flatten()
              print('flattened')
              
              if xyz.isna().any().any()==False:
              # Create DataFrame for current file
                 df = pd.DataFrame({'Time': timestamps , 'X-axis':x , 'Y-axis':y ,'Z-axis':z})
                 print('dataframe')
              # Append DataFrame to list
                 xyzdf.append(df)

                 # ecgdf_concatenated = pd.concat(xyzdf, ignore_index=True)
    
    
    xyzdf_concatenated = pd.concat(xyzdf, ignore_index=True)
    
    
    Time=xyzdf_concatenated['Time'].values
    files_sorted_by_mtime = sorted(Time)
    slicedtime=[(str(times))[:-3] for times in Time]
    slicedtime=[(int(times)) for times in slicedtime]
    timesinseconds=pd.to_datetime(slicedtime,unit='s')
    xyzdf_concatenated['New Time']=timesinseconds
    #sort time
    xyzdf_concatenated.set_index('New Time', inplace=True)
    # Sort DataFrame by index (epochs)
    xyzdf_concatenated.sort_index(inplace=True)

           
    if len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1])) == 5:
       print('The length of recording is 5 days,concatenated files for 5 days')

    elif len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1])) == 6:
         print('The length of recording is 6 days,concatenating files for 6 days')
                     
    elif len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1])) == 7:
         print('The length of recording is 7 days,concatenating files for 7 days')    

    elif len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1])) <= 4:
         print(f'"The length of recording is {len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1]))},concatenating files for {len(pd.date_range(start=timesinseconds[0],end=timesinseconds[-1]))} days  "')
    
    
     
    return xyzdf_concatenated





















