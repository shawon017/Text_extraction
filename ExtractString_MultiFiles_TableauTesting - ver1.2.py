# Code to extract matched and non-matched strings from file.
# importing libraries
import os
import re
import json
# defining location of parent folder
BASE_DIRECTORY = 'C:\Shell'
output_file = open('C:\Shell\Output\Output.txt', 'w')
output = {}
file_list = []
fileList = []
fileList2 = []
contents = ""
lines_seen = set()
string_teamspace= r'(https?://teamspace.slb.com.+?[\'|,|;])+'
def Matched_str():
    # scanning through sub folders

    for (dirpath, dirnames, filenames) in os.walk(BASE_DIRECTORY):
        for f in filenames:
            flag = 0
            if 'xml' in str(f):
                contents = open(os.path.join(str(dirpath), str(f)), encoding="utf8").readlines()

                for line in contents:
                    m = re.findall(string_teamspace , line)
                    if m:

                        fileList2.extend(m)
                        for line in fileList2:
                            if line not in lines_seen:
                                output_file.write(str(f) + ";" + str(m))
                                output_file.write("\n")
                                lines_seen.add(line)






def nonMatched_str():
    # scanning through sub folders

    for (dirpath, dirnames, filenames) in os.walk(BASE_DIRECTORY):
        for f in filenames:
            flag = 0
            if 'xml' in str(f):
                contents = open(os.path.join(str(dirpath), str(f)), encoding="utf8").readlines()

                for line in contents:
                    m = re.findall(string_teamspace , line)
                    if m:
                        flag = 1
                        fileList2.extend(m)
                        for line in fileList2:

                            if line not in lines_seen:
                                output_file.write(str(os.path.join(str(dirpath), str(f))) + ";" + str(m))
                                output_file.write("\n")
                                lines_seen.add(line)
                if not flag:
                    output_file.write(str(os.path.join(str(dirpath), str(f))) + ";")
                    output_file.write("\n")
                    flag = 0

# get user choice for match and non-match
choice = input('Enter 1 for matched string and 0 for non-matched one: ')
if choice == '1':
    Matched_str()
else:
    nonMatched_str()

