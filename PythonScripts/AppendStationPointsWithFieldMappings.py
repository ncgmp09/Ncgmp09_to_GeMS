import arcpy, shutil
from arcpy import env

# Set the workspace environment
#
#env.workspace = "C:\\Documents\\azgs\\mixed"

# List all file geodatabases in the current workspace 
# 
workspaces = arcpy.ListWorkspaces("*", "")
for workspace in workspaces:
    name = arcpy.Describe(workspace).name
    namepart = name.split(".")
    newname = namepart[0]
    # Set local variables
    #
    featureclassin = "Stations"
    featureclassout = "Stations"
    inFC = "C:\\Users\\lbookman\\Documents\\ncgmp\\" + name + "\\GeologicMap\\" + featureclassin
    outFC = "C:\\Users\\lbookman\\Documents\\GeMS\\"+newname+".gdb\\GeologicMap\\" + featureclassout
    schemaType = "NO_TEST"
    subtype = ""

    # Set input field variables
    #
    infield1 = "Stations_ID"
    infield2 = "FieldID"
    infield3 = "Label"
    infield4 = "PlotAtScale"
    infield5 = "MapX"
    infield6 = "MapY"
    infield7 = "DataSourceID"
    infield8 = "GPSX"
    infield9 = "GPSY"
    infield10 = "PDOP"
    infield11 = "SignificantDimensionMeters"
    infield12 = "TimeDate"
    infield13 = "MapUnit"
    infield14 = "Observer"
    infield15 = "LocationConfidenceMeters"

    # Set output field variables
    #
    outfield1 = "Stations_ID"
    outfield2 = "FieldID"
    outfield3 = "Label"
    outfield4 = "PlotAtScale"
    outfield5 = "MapX"
    outfield6 = "MapY"
    outfield7 = "DataSourceID"
    outfield8 = "GPSX"
    outfield9 = "GPSY"
    outfield10 = "PDOP"
    outfield11 = "SignificantDimensionMeters"
    outfield12 = "TimeDate"
    outfield13 = "MapUnit"
    outfield14 = "Observer"
    outfield15 = "LocationConfidenceMeters"

    print "Adding " + featureclassin + " field map to. . ." + workspace
    # Create a fieldmappings object and two fieldmap objects
    #
    input1 = arcpy.FieldMap()
    input2 = arcpy.FieldMap()
    input3 = arcpy.FieldMap()
    input4 = arcpy.FieldMap()
    input5 = arcpy.FieldMap()
    input6 = arcpy.FieldMap()
    input7 = arcpy.FieldMap()
    input8 = arcpy.FieldMap()
    input9 = arcpy.FieldMap()
    input10 = arcpy.FieldMap()
    input11 = arcpy.FieldMap()
    input12 = arcpy.FieldMap()
    input13 = arcpy.FieldMap()
    input14 = arcpy.FieldMap()
    input15 = arcpy.FieldMap()
    
    
    fieldmappings = arcpy.FieldMappings()

    # Add input fields
    #   to fieldmap object.
    #
    input1.addInputField(inFC,infield1)
    input2.addInputField(inFC,infield2)
    input3.addInputField(inFC,infield3)
    input4.addInputField(inFC,infield4)    
    input5.addInputField(inFC,infield5)
    input6.addInputField(inFC,infield6)
    input7.addInputField(inFC,infield7)
    input8.addInputField(inFC,infield8)
    input9.addInputField(inFC,infield9)
    input10.addInputField(inFC,infield10)    
    input11.addInputField(inFC,infield11)
    input12.addInputField(inFC,infield12)
    input13.addInputField(inFC,infield13)
    input14.addInputField(inFC,infield14)
    input15.addInputField(inFC,infield15)

    # Set the Name of the Field output from this field map.
    #
    output1 = input1.outputField
    output1.name = (outfield1)
    input1.outputField = output1
    # Set the Name of the Field output from this field map.
    #
    output2 = input2.outputField
    output2.name = (outfield2)
    input2.outputField = output2
    # Set the Name of the Field output from this field map.
    #
    output3 = input3.outputField
    output3.name = (outfield3)
    input3.outputField = output3
    # Set the Name of the Field output from this field map.
    #
    output4 = input4.outputField
    output4.name = (outfield4)
    input4.outputField = output4
    # Set the Name of the Field output from this field map.
    #
    output5 = input5.outputField
    output5.name = (outfield5)
    input5.outputField = output5
    # Set the Name of the Field output from this field map.
    #
    output6 = input6.outputField
    output6.name = (outfield6)
    input6.outputField = output6
    # Set the Name of the Field output from this field map.
    #
    output7 = input7.outputField
    output7.name = (outfield7)
    input7.outputField = output7    
     # Set the Name of the Field output from this field map.
    #
    output8 = input8.outputField
    output8.name = (outfield8)
    input8.outputField = output8 
     # Set the Name of the Field output from this field map.
    #
    output9 = input9.outputField
    output9.name = (outfield9)
    input9.outputField = output9 
     # Set the Name of the Field output from this field map.
    #
    output10 = input10.outputField
    output10.name = (outfield10)
    input10.outputField = output10 
     # Set the Name of the Field output from this field map.
    #
    output11 = input11.outputField
    output11.name = (outfield11)
    input11.outputField = output11 
     # Set the Name of the Field output from this field map.
    #
    output12 = input12.outputField
    output12.name = (outfield12)
    input12.outputField = output12 
     # Set the Name of the Field output from this field map.
    #
    output13 = input13.outputField
    output13.name = (outfield13)
    input13.outputField = output13 
     # Set the Name of the Field output from this field map.
    #
    output14 = input14.outputField
    output14.name = (outfield14)
    input14.outputField = output14 
     # Set the Name of the Field output from this field map.
    #
    output15 = input15.outputField
    output15.name = (outfield15)
    input15.outputField = output15 
    
    # Add the custom fieldmaps into the fieldmappings object.
    #
    fieldmappings.addFieldMap(input1)
    fieldmappings.addFieldMap(input2)
    fieldmappings.addFieldMap(input3)
    fieldmappings.addFieldMap(input4)
    fieldmappings.addFieldMap(input5)
    fieldmappings.addFieldMap(input6)
    fieldmappings.addFieldMap(input7)
    fieldmappings.addFieldMap(input8)
    fieldmappings.addFieldMap(input9)
    fieldmappings.addFieldMap(input10)
    fieldmappings.addFieldMap(input11)
    fieldmappings.addFieldMap(input12)
    fieldmappings.addFieldMap(input13)
    fieldmappings.addFieldMap(input14)
    fieldmappings.addFieldMap(input15)

    try:
        print "Appending data. . ."
        # Process: Append the feature classes into the empty feature class
        arcpy.Append_management(inFC, outFC, schemaType, fieldmappings, subtype)

    except:
        # If an error occurred while running a tool print the messages
        print arcpy.GetMessages()

    print "Append data to " + featureclassout + " " + newname + " complete. . ."

