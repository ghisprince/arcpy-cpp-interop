
ArcGIS geoprocessing tools have rich support for messaging and reporting
progress within the ArcGIS family of applications.  Within python script
this coding patterns are well established and documented.

The code within this repo shows how to do this from a c++ dll, as well 
as running code within the dll if the user has cancelled the operation.

### Basic flow of code
1. gptool_script.py calls my_cpp_function in the dll with two arguments
  1. a string to show passing argument from python to the dll
  1. a callback function for the dll to push feedback to python
1. my-lib.dll my_cpp_function calls back into python to 
  1. push messages (strings)
  1. move the progress bar


### To use with ArcMap

1. open my-lib.sln
1. in the BUILD menu, select *Configuration Manager...*
  1. set the *Active solution configuration* to Release 
  1. set the *Active solution platform* to Win32
1. build my-lib.dll
1. run gptool_script.py using python27 (to test)
1. Open ArcGIS Pro
  1. add arcpy-cpp-interop.pyt to the project 
  1. run the 'cpp interop example' tool (note progress & messaging)
  


### To use with ArcGIS Pro

1. open my-lib.sln using Visual Studio
1. in the BUILD menu, select *Configuration Manager...* 
  1. set the *Active solution configuration* to Release 
  1. set the *Active solution platform* to x64
1. build my-lib.dll
1. run gptool_script.py using python34 (to test)
1. Open ArcGIS Pro
  1. add arcpy-cpp-interop.pyt to the project 
  1. run the 'cpp interop example' tool (note progress & messaging)


[Tool progress and messages!](tool.png?raw=True )

Notes
At ArcGIS 10.4 (and Pro 1.1) the [arcpy.env.autoCancelling] and 
[arcpy.env.isCancelled] have been added. By setting 
```arcpy.env.autoCancelling = False``` the code in the dll is able to 
run code based on the user having hit *cancel* on the operation
```arcpy.env.isCancelled = True``` .

At versions preceding those mentioned above, there is no easy querying
to determine if user has cancelled the operation, but the rest of the
code, showing messaging, progress, are valid.


Reference
---------
* [Python ctypes documentation]
* [The extern "C" solution]


[arcpy.env.autoCancelling]:http://pro.arcgis.com/en/pro-app/tool-reference/environment-settings/autoCancelling.htm
[arcpy.env.isCancelled]:http://pro.arcgis.com/en/pro-app/tool-reference/environment-settings/isCancelled.htm
[Python ctypes documentation]:https://docs.python.org/2/library/ctypes.html
[The extern "C" solution]:http://www.tldp.org/HOWTO/C++-dlopen/thesolution.html
