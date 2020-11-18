import os
import time
from pathlib import Path
import fnmatch
import subprocess

#The proceeding block of code identifies any FILE.tar.gz within the current directory 
#Then assigns the abspath of that FILE.tar.gz to the var OpenSSL_Tarball_Path
for file in os.listdir('.'):
	if fnmatch.fnmatch(file, '*.tar.gz'):
		OpenSSL_Tarball_Path = os.path.abspath(file)


#This block of code prints a message, waits 5 secs, extracts OpenSSL_Tarball_Path, inserts extracted tarball contents into /OpenSSL, then prints message
#Time.sleep intervals along with new lines are inserted throughout this script for the sake of aesthetics
print('Extraction Of OpenSSL Tarball Has Now Commenced...')
time.sleep(5)
subprocess.call(["tar", "-xvf", OpenSSL_Tarball_Path, "--strip-components=1", "-C", "OpenSSL"])
print('\n')
print('OpenSSL Has Been Successfully Extracted')
time.sleep(3)

#Command that changes dir into the pre-made /OpenSSL, where the extracted tarball contents are now located
os.chdir('OpenSSL')

#New lines seperate tar extraction step and initiates ./config step
print('\n')
print('\nBeginning OpenSSL Configuration...')
time.sleep(3)
os.system('./config')

#Prints message and initiates make step
print('\n')
print('\n')
print('\nCreating Makefile...')
time.sleep(3)
os.system('make')

#Prints message and initiates make test step
print('\n')
print('\n')
print('\nInitiating Testing Of Makefile...')
time.sleep(3)
os.system('make test')
print('\n')
print('\nMakefile Looks Good, Proceeding With Install...')

#Prints message and initiates make install step
time.sleep(3)
print('\n')
print('\n')
print('\nNow Installing OpenSSL, Please Wait...') 
time.sleep(3)
os.system('make install')

#Updates lib conf files
print('\n')
print('\n')
print('Updating And Binding Lib Conf Files, Please Wait...')
subprocess.call(["ldconfig", "/usr/lib", "/etc/ld.so.conf.d/libc.conf"])
print('Binding completed')

#Final successfull compilation message
print('\n')
print('\n')
print('Congratulations, OpenSSL Has Been Successfully Compiled & Installed')
time.sleep(3)
