import os
import subprocess
import shutil

import sys

directory = '../../data/game_data'


subfolders = [ f.path for f in os.scandir(directory) if f.is_dir() ]

for folder in subfolders:
    bevent = r'../bevent/BEVENT.EXE'
    shutil.copyfile(bevent, f'{folder}/BEVENT.EXE')

    year = folder[-7:-3]


    # Create a folder to store the processed event logs
    if not os.path.isdir('../../data/processed_events'):
        os.makedirs('../../data/processed_events')
    
    event_files = os.listdir(folder)
    for file in event_files.copy():
        if file[-3:] == 'EVA' or file[-3:] == 'EVN':
            continue
        
        else:
            event_files.remove(file)

    for file in event_files:
        team = file
        process = subprocess.Popen([f'wine {folder}/BEVENT.EXE -y {year} -f 0,10,11,14,15,26,27,28,32,34,43,59,60,61,66,67,68 {folder}/{file} > ../../data/processed_events/{file[:-4]}.txt'], shell=True)
        
        
process.terminate()
    



    #os.remove(f'{folder}/BEVENT.EXE')


