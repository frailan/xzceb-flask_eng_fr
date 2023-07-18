"""
File Copy Utility

This script copies a file from a source location to a destination folder.
"""

import shutil

SOURCE_FILE_PATH = 'tests.py'
DESTINATION_FOLDER_PATH = 'machinetranslation'

shutil.copy2(SOURCE_FILE_PATH, DESTINATION_FOLDER_PATH)
