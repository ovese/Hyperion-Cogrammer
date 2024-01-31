import json
import os

calc_json_info = {
    "A" : "Investment",
    "B" : "Bond"
}
myCalcJSON = json.dumps(calc_json_info)

with open("fin_calc_conf.json", "w") as jsonfile:
    jsonfile.write(myCalcJSON)
    
    jsonfile = os.path.basename("fin_calc_conf.json")
    print(f"Write successful to json file {jsonfile}")
    

"""starting config file patch
    for the ini file type
"""
from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

# Assume we need 2 sections in the config file, 
# let's call them xxxxINFO and xxxxCONFIG
# however I have changed this and used mine
config_object["CALCINFO"] = {
    "A": "Investment",
    "B": "Bond"
}

#Write the above sections to config.ini file
with open('fin_calc_conf.ini', 'w') as conf:
    config_object.write(conf)
    
    inifile = os.path.basename("fin_calc_conf.ini")
    print(f"Write successful to json file {inifile}")