import sys
import main

if len(sys.argv)  < 3:
    print("Invalid number of arguments passed:")
    quit()
type = sys.argv[1]
if type=="-u" or type =="-U":
    if sys.argv[2] == "-r" or  sys.argv[2] == "-r":
        main.user_info(sys.argv[3],True)
    else:
        main.user_info(sys.argv[2],False)
if  type=="e" or type=="E":
    if sys.argv[2]==""


        