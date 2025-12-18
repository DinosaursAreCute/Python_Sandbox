import logging
import types
from pathlib import *
import pickle
print(pickle.__doc__)
import colorama as color

import Utils.Logger as Logger
import ioHelper.fileOperations as fOps

if __name__ == "__main__":

    log = Logger.LoggerClass(logger_name="TestLogger",logger_level = 1,log_color = True)

    log.info("Starting testing...")
    log.info("Converting string to path object")
    path = fOps.convert_string_to_path("Test/Test_1/Test_2_file.txt")
    log.info("converting another string to path object")
    target_path= fOps.convert_string_to_path(f"Test/{path.parts[-1]}")
    subdirMap=fOps.list_subdirectories(path,True)
    for x in subdirMap:
        files=fOps.list_files(x)

    print(fOps.list_subdirectories(root_path = path).__doc__)
    fOps.move_file(path,f"Test/{path.parts[-1]}",True,True)
    fOps.copy_file(target_path,path,False,False)
    fOps.rename_file(path,"Test_3_file.txt",True)