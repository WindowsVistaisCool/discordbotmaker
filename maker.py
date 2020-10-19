import json

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
def setup()
  print(f"To make a discord bot, you first need to go to {clr.UNDERLINE}https://discord.com/developers/applications/{clr.e} and click 'New Application' and type the name of your bot in the field.\nNext, click the 'bot' tab on the left hand side and click create bot.\nThen just under the name/discriminator(number) is the token. Click copy and then paste it in the field below:\n")
  tken = input("Paste or enter your token: ")
  if len(tken) > 0:
    wjson('config.json', 'token' tken)
    print("Token accepted!")
  else:
    setup()

def setupstatus(statinput, activity):
  if len(statinput) > 0:
    if statinput == "ONL":
      if activity == "Game":
        wjson('config.json', 'activity', 'G')
        wjson('config.json', 'status', 'ONL')
      elif activity == "Watching":
        wjson('config.json', 'activity', 'W')
        wjson('config.json', 'status', 'ONL')
      elif activity == "Listening":
        wjson('config.json', 'activity', 'L')
        wjson('config.json', 'status', 'ONL')
      else:
        print(f'{clr.r}{clr.BOLD}ERROR{clr.e}\n{clr.r}The specified activity was not found{clr.e}")
    elif statinput == "IDL":
      if activity == "Game":
        wjson('config.json', 'activity', 'G')
        wjson('config.json', 'status', 'IDL')
      elif activity == "Watching":
        wjson('config.json', 'activity', 'W')
        wjson('config.json', 'status', 'IDL')
      elif activity == "Listening":
        wjson('config.json', 'activity', 'L')
        wjson('config.json', 'status', 'IDL')
      else:
        print(f'{clr.r}{clr.BOLD}ERROR{clr.e}\n{clr.r}The specified activity was not found{clr.e}")
    elif statinput == "DND":
      if activity == "Game":
        wjson('config.json', 'activity', 'G')
        wjson('config.json', 'status', 'DND')
      elif activity == "Watching":
        wjson('config.json', 'activity', 'W')
        wjson('config.json', 'status', 'DND')
      elif activity == "Listening":
        wjson('config.json', 'activity', 'L')
        wjson('config.json', 'status', 'DND')
      else:
        print(f'{clr.r}{clr.BOLD}ERROR{clr.e}\n{clr.r}The specified activity was not found{clr.e}")
    else:
      print(f'{clr.r}{clr.BOLD}ERROR{clr.e}\n{clr.r}The specified status was not found{clr.e}")
            
  else:
    setcirclestatus(activity)
    
def setcirclestatus(nameact):
  if nameact == "Streaming":
    wjson('config.json', 'activity', 'S')
    wjson('config.json', 'status', 'STR')
  else:
    print('Now, you need to set the status of the bot. Type "ONL" for online, "IDL" for afk/idle, or "DND" for Do not Disturb.")
    stat = input("Status: ")
    setupstatus(stat, nameact)
          
def setstatus():
  print(f'{clr.g}Type "Game" for game activity, "Streaming" for streaming activity, "Watching" or "Listening" for a watching/listening activity, or "None" for no activity{clr.e}')
  act = input("Activity Type: ")
  if len(act) > 0:
    if act == "None":
      pass
    elif act == "Game":
      print("Please enter the name of your game (will display as 'Playing [game]')")
      actname = input("Game name: ")
      if len(actname) > 0:
        pass
      else:
        actname = input("Game name: ")
    elif act == "Streaming":
      print("Please provide a stream URL so the link will work")
      strurl = input("URL: ")
      if len(strurl) > 0:
        pass
      else:
        strurl = input("URL: ")
      print("Please enter the stream name (will show up as Streaming [name])")
      actname = input("Stream Name: ")
      if len(actname) > 0:
        pass
      else:
        actname = input("Stream Name: ")
    elif act == "Watching":
      print("Please enter the name of the watching activity (will show up as Watching [name])")
      actname = input("Name: ")
      if len(actname) > 0:
        pass
      else:
        actname = input("Name: ")
    elif act == "Listening":
      print("Please enter the name of the listening activity (will show up as Listening to [name])")
      actname = input("Name: ")
      if len(actname) > 0:
        pass
      else:
        actname = input("Name: ")
  else:
    setstatus()
  setcirclestatus(act)
          
def main():
  setup()
  
