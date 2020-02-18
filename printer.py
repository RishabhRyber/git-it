from colorama import Fore, Back, Style

def print_color(text="dummy",text_color="",back_color=""):
  
  
  if text_color == "red":
    text_color = Fore.RED
  elif text_color == "green":
    text_color = Fore.GREEN
  elif text_color == "blue":
    text_color = Fore.BLUE
  elif text_color == "green":
    text_color = Fore.GREEN
  else:
    text_color = Fore.RESET
  
  
  if back_color == "red":
    back_color =  Back.RED
  elif back_color == "green":
    back_color = Back.GREEN
  elif back_color  == "blue":
    back_color = Back.BLUE
  elif back_color == "green":
    back_color = Back.GREEN
  else:
    back_color = Back.RESET
  
  print(text_color + back_color + text)
print_color("jhejdfjdf","green")