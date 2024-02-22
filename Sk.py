#coding=utf-8
import os, sys, platform
os.system('rm -rf MAHIN')
os.system('git pull')
try:
    if sys.argv[1]=='MAHINX':
        os.system('rm -rf MAHIN')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ALL'):
        os.system('curl -L https://github.com/MAHIN-404/MAHIN-404/blob/main/MAHIN?raw=true -o MAHIN')
        os.system('chmod 777 MAHIN;./MAHIN')
    else:
        os.system('chmod 777 MAHIN;./MAHIN')
