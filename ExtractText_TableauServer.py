import os
import re

BASE_DIRECTORY = 'C:\Shell'
output_file = open('C:\Shell\Output\Output.txt', 'w')
output = {}

lines_seen = set()
string_teamspace = r'(https?://teamspace.slb.com.+?[\'|,|;])+'
contents = ""
def Matched_str():
    for (dirpath, dirnames, filenames) in os.walk(BASE_DIRECTORY):
        for f in filenames:
            if 'xml' in str(f):
                contents = open(os.path.join(str(dirpath), str(f)), encoding="utf8").readlines()

                for line in contents:
                    m = re.findall(string_teamspace, line)
                    if m:
                        file_list = []
                        file_list.extend(m)
                        lines = file_list[0]
                        if lines not in lines_seen:
                            output_file.write(str(os.path.join(str(dirpath), str(f))) + ";" + str(m))
                            output_file.write("\n")
                            lines_seen.add(lines)
                            del file_list[:]


def NonMatched_str():
    for(dirpath, dirnames, filenames) in os.walk(BASE_DIRECTORY):
        for f in filenames:
            file_list = []
            flag=0
            if 'xml' in str(f):
                contents = open(os.path.join(str(dirpath), str(f)), encoding="utf8").readlines()
                for line in contents:
                    m = re.findall(string_teamspace, line)
                    if m:
                        file_list.extend(m)
                        flag=1
                        line = file_list[0]
                        if line not in lines_seen:
                            output_file.write(str(os.path.join(str(dirpath), str(f))) + ";" + str(m))
                            output_file.write("\n")
                            lines_seen.add(line)
                            del file_list[:]
                if not flag:
                    output_file.write(str(os.path.join(str(dirpath), str(f))) + ";")
                    output_file.write("\n")
                    flag=0

choice = input('1 for mathed string: ')
if choice == '1':
    Matched_str()
else:
    NonMatched_str()
