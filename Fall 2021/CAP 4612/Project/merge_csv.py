#!/bin/python
import pandas as pd;
import os
import random as rd
import threading as th

training_df = pd.DataFrame();
testing_df = pd.DataFrame()
random = rd.Random()
threads = []

def loadToMem(df: pd.DataFrame, fileName: str):
    for i,row in df.iterrows():
        picked = random.randrange(0,100)
        if picked < 20:
            testing_df.append(row)
        else:
            training_df.append(row)
    print(f'File: {fileName} DONE!')
                
for file in os.listdir(os.getcwd()):
    print(f'Working on File: {file}')
    if(file.endswith('.csv')):
        file_df = pd.read_csv(file)
        print(f'Loaded Entries (Rows): {len(file_df.index)}')
        thread = th.Thread(target=lambda: loadToMem(file_df, file))
        threads.append(thread)
        thread.start()

print('All Files Loaded, Waiting on threads!')
for thread in threads:
    thread.join()
               
print('Filling in empty spaces with "N/A"')        
training_df.fillna(value='na', axis=0,inplace=True)
testing_df.fillna(value='na', axis=0,inplace=True)
print(f'Training Data # Rows: {len(training_df.index)}')
training_df.to_csv('training_merged.csv')
print(f'Testing Data # Rows: {len(testing_df.index)}')
testing_df.to_csv('testing_merged.csv')
