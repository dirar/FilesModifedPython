#!/usr/bin/env python

import os, sys, time
from datetime import timedelta, datetime

totalFiles1 = 0;
totalFilesSize1 = 0;
totalFiles2 = 0;
totalFilesSize2 = 0;
days = 0;
daysts = 0;

def checkModificationDates(path):
    global totalFiles1, totalFilesSize1,totalFiles2, totalFilesSize2, days, daysts
    totalsize1 = float();
    files1 = 0;
    totalsize2 = float();
    files2 = 0;
     
    for directory, subdirectories, filenames in os.walk(path):
        for filename in filenames:
            full_filename = os.path.join(directory, filename);
            unix_timestampc = float(os.path.getmtime(full_filename));
            mod = time.ctime(os.path.getmtime(full_filename)) ;
            filesize = os.stat(full_filename).st_size;
            
            if unix_timestampc >= daysts:
                totalsize1 += filesize;
                files1 += 1
                totalFilesSize1 += filesize;
                totalFiles1 += 1;               
            else:
                totalsize2 += filesize;
                files2 += 1;
                totalFilesSize2 += totalsize2;
                totalFiles2 += 1;
    
    print("Files in %s modified within %s days: [%s files, %s bytes]" % (path,days, files1,totalsize1));
    print("Total files number in %s : %s size %s bytes" % (path,files1+files2,totalsize1+totalsize2));
    print("\n******************************************\n");
    
if __name__ == '__main__':
    if len(sys.argv) > 2:
        days = int("0" + sys.argv[1]);
        now = time.time();
        daysts = now - 60*60*24*days;
        folders = sys.argv[2:]
        for i in folders:
            # Iterate the folders given
            if os.path.exists(i):
                checkModificationDates(i)                
            else:
                print('%s is not a valid path, please verify' % i)
                sys.exit()
        
        print("Files in all pathes modified within %s days: [%s files, %s bytes]" % (days, totalFiles1,totalFilesSize1));
        print("Total files number all pathes: %s size %s bytes" % (totalFiles1+totalFiles2,totalFilesSize1+totalFilesSize2));
    else:
        print('Usage: days path1 path2 path3...');