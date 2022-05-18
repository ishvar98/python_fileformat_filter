##To list specific file format with file size in a specific directory

import os, fnmatch

#Replace directory path name in ""
directory="C:/XXXX/XXXX/XXXX/"

fileOfDirectory = os.listdir(directory)

#Replace pattern in ""
#ex.    = "*.zip"

pattern = "*.txt"

i=1

fmt=pattern

rfmt=fmt.replace("*.","")

print("Displaying files with extension of",rfmt,"in",directory)
for filename in fileOfDirectory:
    if fnmatch.fnmatch(filename, pattern):

            os.chdir(directory)
            size = os.stat(filename).st_size

            print("============================================")
            print("||File    ||",i)
            print("--------------------------------------------")
            print("||Filename||",filename,"")
            print("--------------------------------------------")
            print("||Size    ||",size,"bytes")
            print("============================================")
            print("")
            i=i+1;
