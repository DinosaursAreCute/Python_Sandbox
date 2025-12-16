import types
from pathlib import *

import colorama as color

import Utils.Logger as Logger
import ioHelper.fileOperations as fOps

if __name__ == "__main__":

    log1 = Logger.LoggerClass(logger_name="TestLogger",logger_level = 0,log_color = True)

    log1.log_message("DEBUG",0)
    log1.log_message("VALUE",1)
    log1.log_message("INFO",2)
    log1.log_message("SUCCESS",3)
    log1.log_message("WARNING",4)
    log1.log_message("ERROR",5)

    test = color.Fore.RED+'Hello world'+color.Fore.RESET
    print(test)