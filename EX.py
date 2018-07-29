# Code to extract matched and non-matched strings from file.
# importing libraries
import os
import re
# import AlteryxPythonSDK as sdk
# defining location of parent folder
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_file = open(os.path.join(__location__, 'user_input.txt'))

BASE_DIRECTORY = open(os.path.join(__location__, 'file_directory.txt'))
file_format = open(os.path.join(__location__, 'file_format.txt'))

file_name = "teamspace.txt"
output_file = open(file_name, 'w')
# input_file = open(r"C:\Users\MPathan4\OneDrive - Schlumberger\SSO DnA\Internship\Alteryx\TextExtraction_app\user_input.txt")
user_string =""
source_directory=""
file_formats=""
for line in input_file.read():
    if line is not '\n':
        user_string = user_string + line
for line in BASE_DIRECTORY.read():
    if line is not '\n':
        source_directory = source_directory + line
for line in file_format.read():
    if line is not '\n':
        file_formats = file_formats + line

file_formats = file_formats.split()
items = 0
user_output = {}
file_list = []
fileList = []
fileList2 = []
contents = ""
lines_seen = set()
user_input=str(user_string)
string_teamspace= r'(https?://.+?[]\',;".])+'
string_teamspace = string_teamspace[:10] + user_input + string_teamspace[10:]
print (string_teamspace, source_directory)
def Matched_str():
    # scanning through sub folders

    for (dirpath, dirnames, filenames) in os.walk(source_directory):
        for f in filenames:
            flag = 0
            if 'xml' in str(f):
                contents = open(os.path.join(str(dirpath), str(f)), encoding = "utf8").readlines()

                for line in contents:
                    m = re.findall(string_teamspace , line)
                    if m:

                        fileList2.extend(m)
                        for line in fileList2:
                            if line not in lines_seen:
                                output_file.write(str(os.path.join(str(dirpath), str(f))) + ";" + str(m))
                                output_file.write("\n")
                                lines_seen.add(line)



    output_file.close

Matched_str()

