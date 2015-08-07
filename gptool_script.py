"""
This script shows

#1: communication between python & dll
     - pushing unicode/str and integers to/from python & dll
     - callback from dll into python
        - dll code driving progress dialog
        - dll code pushing messages to gp framework

#2: use of the autoCancelling/isCancelled* which allow code in the dll to
     callback into python/arcpy's status and determine if user has
     cancelled operation (allows code within the dll to deal with cancel)

*ArcGIS 10.4 (Pro 1.1) is the first release which has
autoCancelling/isCancelled, but code below will work with older
versions as well.
"""

import arcpy
import platform
import ctypes
import os
import sys


# path to dll (based on MS Visual Studio 2013)
# this path will vary based on compiler settings
# so update the line below
#  - x32 vs x64
#  - Release vs Debug

dll_path = r"my-lib\Release\my-lib.dll"
if platform.architecture()[0] == "64bit":
    dll_path = dll_path.replace("Release", "x64\\Release")

dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), dll_path)

if not os.path.isfile(dll_path):
  arcpy.AddError("Could not find dll {}".format(dll_path))
  arcpy.AddError("Update gp_script.py line 32")
  sys.exit(0)


if hasattr(arcpy.env, "autoCancelling"):
    # disable autoCancelling behaviour normally done by ArcGIS
	#  so dll can run code if cancel is requested by user
    arcpy.env.autoCancelling = False
else:
    arcpy.env.isCancelled = False

# callback prototype (one output args followed by 2 inputs)
CALLBACK_C_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int,
                                        ctypes.c_int,
                                        ctypes.c_wchar_p)

# py class that will be called from code within my-lib.dll
class Callback(object):
    """ arcpy's progressor based on info passed from dll """
    def __init__(self):
        arcpy.SetProgressor('step', "Processing", 0, 10, 1)
        self.c_function = CALLBACK_C_PROTOTYPE(self.update)

    def update(self, i, msg):
        arcpy.SetProgressorPosition(i)
        if msg:
            arcpy.AddMessage(msg)

        # return to dll IsCancelled (1 = user clicked cancel)
        return int(arcpy.env.isCancelled)

loaded_dll = ctypes.cdll.LoadLibrary(dll_path)

# Describe function being called in the dll
lib_func = loaded_dll.my_cpp_function
lib_func.argtypes = [ctypes.c_wchar_p, CALLBACK_C_PROTOTYPE]
lib_func.restype = ctypes.c_int


def run():
    # call function in my-lib.dll, Callback passed to lib for communication
    callback = Callback()
    returncode = lib_func(u"String arg from in python", callback.c_function)
    arcpy.AddWarning("RETURN CODE: {} (0=success, 1=error)".format(
                                                                returncode))

if __name__ == "__main__":
    run()
