import datetime
import shutil
import os
import time
#startup notification
print("The program is now running!")
#if you want the program to run until you shut it down manually
automatic=False 


#wether or not you want to copy all files in a directory
allfiles=True

#the path to your save file directory and destination path for backup
copypath=f'C:\\Users\\Public\\Documents\\OnlineFix\\1446780\\Saves\\win64_save'
destpath=f"C:\\Users\\Public\\Documents\\Mhrisebackup"

#these are the names of the files you want to copy in case you dont want to copy all files
files=['data00-1.bin','data001Slot.bin']


while(True):
    
    #returns the local date and time
    localtime=datetime.datetime.today() 
    
    #the function for copying all directory files
    if allfiles!=False:
        for file in os.listdir(copypath):
            if os.path.isfile(f'{copypath}\{file}'):
                files.append(file)
    
    #im naming each save directory with the time of its creation
    dirname="save {date}--{hour}-{minute}-{sec}".format(date=localtime.date(),hour=localtime.hour,minute=localtime.minute,sec=localtime.second)
    os.chdir(destpath)#changing working directory
    os.mkdir(f"{dirname}") #making new save directory
    os.chdir(dirname) #changing working directory
    
    #finally the actual copying process
    for file in files:
        shutil.copy(f'C:\\Users\\Public\\Documents\\OnlineFix\\1446780\\Saves\\win64_save\\{file}',f'{destpath}\{dirname}\{file}')
    #breaks out of the loop for the single use mode
    if automatic!=True:
        break
    #you can setup an automatic backup period
    time.sleep(3) #the period of time between each backup (in seconds)
    
    
