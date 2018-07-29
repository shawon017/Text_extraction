import re
import glob
file = open("c:/Shell/WT to GL Mapping Dashboard.xml","r")

f = file.read()
url = re.findall(r'(https?://teamspace[\w\./]+)+', f)

for urls in url:
    print(url)
                 

