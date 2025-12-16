import logging
from pathlib import *

import Utils.Logger

# ======================== Initialization ========================
log = Utils.Logger.LoggerClass("FileOperationsLogger",logger_level = 0,log_color = True)


# ======================== Common Utils ========================

def convert_string_to_path(target_path):
    log.debug(f"Converting {target_path} to Path object")
    return Path(target_path)


# ======================== Directory Utils ========================#

def check_is_directory(target_directory):
    is_dir= target_directory.is_dir
    log.debug(f"{target_directory} is path = {is_dir}")
    if is_dir:
        log.info(f"{target_directory} is not a directory or does not exist")
        return False
    return True


def check_directory_exists(target_directory):
    if not target_directory.exists():
        log.debug(f"target directory does not exist. Target directory: ({target_directory})")
        return False
    return True


def list_subdirectories(root_path):
    if not check_is_directory(root_path) and check_directory_exists(root_path):
        log.debug("No subdirectories have been found")
        return None
    return root_path.iterdir()


# ======================== File Utils ========================