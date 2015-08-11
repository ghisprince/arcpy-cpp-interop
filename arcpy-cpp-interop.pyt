import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "arcpy-cpp-interop"
        self.alias = "cppinterop"

        # List of tool classes associated with this toolbox
        self.tools = [cppInteropExample]


class cppInteropExample(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "cpp interop example"
        self.description = "Shows progress, messages, and cancelling"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        import gptool_script
        gptool_script.run()
