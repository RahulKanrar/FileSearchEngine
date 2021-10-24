#import modules
import os
import logging


#detecting drives present

def mydrive():
    drives=[]
    for x in range(65,91):
        if os.path.exists(chr(x)+":"):
            drives.append(chr(x))
    print("all drives in my computer are: ",drives)
    return drives

if __name__=='__main__':
    systemdrives=mydrive()
    try:
        print(systemdrives)
    except Exception as Argument:
        logging.exception("Error occured while detecting systemdrives")