.This code pipeline can be run to clean data you get from the Vital patch.
.This code pipeline focused on merging various output logs of signal data from the vital patch into a  single dataframes for each metrics(i.e ECG,Vitals,XYZ) for easier analysis.
.The code pipeline ouputs dataframe with real date time indexes that will make analysis more easier and meaningful than dealing with epoch dates.
.In future modifications,the code will also add up an automatic pipeline to process your ecg logs to get relevant HRV metrics for your analysis.
