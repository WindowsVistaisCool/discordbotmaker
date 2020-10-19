import json
from time import sleep
from os import system

class clr:
  HEADER = '\033[95m'
  b = '\033[94m'
  g = '\033[92m'
  y = '\033[93m'
  r = '\033[91m'
  e = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

def rjson(file, paramtr):
  with open(file, 'r') as v:
    x = json.load(v)
  return x[paramtr]

def wjson(file, paramtr, valu):
  with open(file, 'r') as v:
    x = json.load(v)
  x[paramtr] = valu
  with open(file, 'w') as v:
    json.dump(x, v, indent=4)

def main():
  print(f"{clr.b}Starting Discord Bot Maker...{clr.e}")
  sleep(2)
  system("python3 maker.py")
  
def script_install():
  if rjson('config.json', 'install') == 'yes':
    print(f"{clr.g}FIRST RUN DETECTED{clr.e}\n{clr.y}Installing Repositories{clr.e}")
    system("python3 -m pip install discord.py[voice]")
    wjson('config.json', 'install', 'no')
    main()
  else:
    main()
