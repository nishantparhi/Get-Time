import os
import subprocess
import json

os.system("curl 'http://worldtimeapi.org/api/ip' -s > mytime")


datatoread = ["utc_offset","abbreviation","timezone","datetime"]

for key in time:
        if key in datatoread:
            print("{}: {}".format(key, time[key]))
           
with open("mytime", "r+") as time:
    time = json.loads(time.read())
