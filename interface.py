import sys
import main
argv=sys.argv
if len(argv)==2 and argv[1]=="-h":
  main.show_man()
if len(argv)  < 2:
    print("Invalid number of arguments passed:")
    print("use pyhton git-it -h to get help")
    quit()

type = argv[1]
if type=="-u" or type =="-U":
    if sys.argv[2] == "-r" or  sys.argv[2] == "-r":
        main.user_info(argv[3],True)
    else:
        main.user_info(argv[2],False)
if type == "-e" or type =="-E":
  if sys.argv[2] == "-r" or  sys.argv[2] == "-r":
    main.show_logo()
    main.user_info(main.email_to_id(argv[3]),True)
  else:
    main.show_logo()
    main.user_info(main.email_to_id(argv[2]),False)


      