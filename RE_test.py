import os
import re
file_directory = 'C:\Shell'

output_file = open('C:\Shell\Output\Re_test.txt', 'w')
contents = ""
# def match_str():
#     for(dirpath, dirnames, filenames) in os.walk(file_directory):
#         for f in filenames:
#             contents = open()
with open('C:\Shell\Output\Output.txt', encoding = "utf8") as f:
    for line in f.readlines():
        m = re.findall(r'(^ADSL.+)+', line)
        if m:
            print(m)

