##To list specific file format with file size in a specific directory

import os, fnmatch

#Replace directory path name in ""
directory="C:/Users/Selvakumar/Downloads/"

fileOfDirectory = os.listdir(directory)

#Replace pattern in ""
#ex.    = "*.zip"

pattern = "*.txt"

i=1

for filename in fileOfDirectory:
    if fnmatch.fnmatch(filename, pattern):
            
          #  print(filename)
            os.chdir(directory)
            size = os.stat(filename).st_size
          #  print(size)
            print("============================================")
            print("||File    ||",i)
            print("||Filename||",filename,"")
            print("||Size    ||",size,"bytes")
            print("============================================")
            i=i+1;