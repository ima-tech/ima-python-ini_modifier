import os
import os.path
import sys
import configparser

if len(sys.argv) < 4:
    print('You need four parameters, iniFile, section, option and value')
    sys.exit(0);

# Open the .ini file
iniFile = sys.argv[1]
section = sys.argv[2]
option = sys.argv[3]
value = sys.argv[4]

# create the .ini file if it doesn't exist
if os.path.isfile(iniFile) is False:
    os.makedirs(os.path.dirname(iniFile), exist_ok=True)
    with open(iniFile, "w") as f:
        f.write("")

config= configparser.ConfigParser()
config.read(iniFile)

# verify that the section exist. If not, add it
if config.has_section(section) is False:
    config.add_section(section)

# Get the section, option and value to define in the .ini file
config.set(section, option, value)

with open(iniFile, 'w') as configfile:
    config.write(configfile)