ArcGIS geoprocessing tools have rich support for messaging and reporting
progress within the ArcGIS family of applications.  With script tools 
implemented with python the coding patterns are well established and 
documented.

The code within this repo shows how to call from python to a C/C++ 
library (dll) and have the dll drive the ArcGIS application progressor, 
pass messages to the app, and query if the user has cancelled the 
operation (in order to cancel processing and gracefully exit the dll).



Basic flow of code
------------------

1. gptool_script.py calls my_cpp_function in the dll with two arguments
  1. a string to show passing argument from python to the dll
  1. a callback function for the dll to push feedback to python
1. my-lib.dll my_cpp_function calls back into python to 
  1. push messages (strings)
  1. move the progress bar
  1. query if arcpy.env.isCancelled is True (user has cancelled operation)



To use with ArcMap
------------------

1. open my-lib.sln with Visual Studio
1. in the BUILD menu, select *Configuration Manager...*
  1. set the *Active solution configuration* to Release 
  1. set the *Active solution platform* to Win32
1. build my-lib.dll
1. run gptool_script.py using python27 (to test)
1. Open ArcGIS Pro
  1. add arcpy-cpp-interop.pyt to the project 
  1. run the 'cpp interop example' tool (note progress & messaging)
  


To use with ArcGIS Pro
----------------------

1. open my-lib.sln with Visual Studio
1. in the BUILD menu, select *Configuration Manager...* 
  1. set the *Active solution configuration* to Release 
  1. set the *Active solution platform* to x64
1. build my-lib.dll
1. run gptool_script.py using python34 (to test)
1. Open ArcGIS Pro
  1. add arcpy-cpp-interop.pyt to the project 
  1. run the 'cpp interop example' tool (note progress & messaging)



![Tool progress and messages](tool.png?raw=True )

Notes
-----
At Pro 1.1 (planned for ArcGIS 10.4) the arcpy.env.autoCancelling and 
arcpy.env.isCancelled have been added. By setting 
```arcpy.env.autoCancelling = False``` the code in the dll is able to 
run code based on the user having hit *cancel* on the operation
```arcpy.env.isCancelled = True``` .

Before Pro 1.1/ArcGIS 104, the properties mentioned above are missing 
progress and messaging will work, but the callback will fail if user 
has cancelled the tool, this failure with the Callback could be trapped
for as indication of a cancel situation.


Reference
---------
* [Python ctypes documentation]
* [The extern "C" solution]
* [jasonbot / devsummit2014 repo]
* [ArcGIS doc Calling a DLL from a script tool]

[Python ctypes documentation]:https://docs.python.org/2/library/ctypes.html
[The extern "C" solution]:http://www.tldp.org/HOWTO/C++-dlopen/thesolution.html
[jasonbot / devsummit2014 repo]:https://github.com/jasonbot/devsummit2014
* [ArcGIS doc Calling a DLL from a script tool]:http://desktop.arcgis.com/en/desktop/latest/analyze/creating-tools/calling-a-dll-from-a-script-tool.htm
