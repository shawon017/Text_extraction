# importing libraries
import os
import re
# defining location of parent folder
BASE_DIRECTORY = 'C:\Shell'
output_file = open('C:\Shell\Output\Output.txt', 'w')
##output_file2 = open('C:\Shell\Output\Output_ts.txt', 'w')
output = {}
output2 = {}
file_list = []
fileList = []
fileList2 = []
liness = []

def notMatch_func():
    # scanning through sub folders
    for (dirpath, dirnames, filenames) in os.walk(BASE_DIRECTORY):
        for f in filenames:
            if 'xml' in str(f):
                contents = open(os.path.join(str(dirpath), str(f)), encoding="utf8").read()
##                if 'http://teamspace.slb.com' in contents:
##                    print(contents)
                m = re.findall(r'(https?://teamspace[\w\./]+)+', contents)
##                m = re.findall(r'(https?://ts.slb.com[\w\./]+)+', contents)
                if m:
                    fileList.append(os.path.join(str(dirpath), str(f)))
##                    output[fileList] = []
##                    output[fileList].append(m)
                    
                  

    for file in fileList:
        txtfile = open(file, 'r', encoding="utf8")
        output[file] = []
        for line in txtfile:
            if 'http://teamspace' in line:
                output[file].append(line)


def match_func():
    # scanning through sub folders
    for (dirpath, dirnames, filenames) in os.walk(BASE_DIRECTORY):
        for f in filenames:
            e = os.path.join(str(dirpath), str(f))
            fileList.append(e)
        for ff in fileList:
            txtfile = open(ff, 'r', encoding="utf8")
            output[ff] = []
            for line in txtfile:
                if 'xml' in str(filenames) and 'http:\\teamspace.slb.com' in line:
                    r = os.path.join(str(dirpath), str(filenames))
                    output[ff].append(r)
                    output[ff].append(line)
                    print("1")
             

                
                
# get user choice for match and non-match
choice = input('Enter 1 for matched string or 0 for non_matched ones: ')
if choice == '1':
    match_func()
elif choice == '0':
    notMatch_func()


tabs = []
for tab in output:
    tabs.append(tab)
    

tabs.sort()
for tab in tabs:
##    print(tab)
    output_file.write(tab + '\n')
##    output_file2.write(tab + '\n')
    output_file.write('\n')
##    output_file2.write('\n')
    for row in output[tab]:
        output_file.write(row + '')
##        output_file2.write(row + '')
    output_file.write('\n')
##    output_file2.write('\n')
    output_file.write('----------------------------------------------------------\n')
##    output_file2.write('----------------------------------------------------------\n')

#raw_input()
