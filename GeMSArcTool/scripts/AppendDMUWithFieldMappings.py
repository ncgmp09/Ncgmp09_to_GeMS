import arcpy, shutil
from arcpy import env

# Set the workspace environment
#
# List all file geodatabases in the current workspace 
# 
#workspaces = arcpy.ListWorkspaces("*", "")
#for workspace in workspaces:
#name = arcpy.Describe(workspace).name
#namepart = name.split(".")
#newname = namepart[0]
# Set local variables
#
featureclassin = "DescriptionOfMapUnits"
featureclassout = "DescriptionOfMapUnits"
inFC = arcpy.env.ncgmp09 + "\\" + featureclassin
outFC = arcpy.env.gems + "\\" + featureclassout
schemaType = "NO_TEST"
subtype = ""

# Set input field variables
#
infield1 = "DescriptionOfMapUnits_ID"
infield2 = "MapUnit"
infield3 = "Label"
infield4 = "Name"
infield5 = "FullName"
infield6 = "Age"
infield7 = "Description"
infield8 = "HierarchyKey"
infield9 = "ParagraphStyle"
infield10 = "AreaFillRGB"
infield11 = "GeneralLithologyConfidence"
infield12 = "DescriptionSourceID"

# Set output field variables
#
outfield1 = "DescriptionOfMapUnits_ID"
outfield2 = "MapUnit"
outfield3 = "Label"
outfield4 = "Name"
outfield5 = "FullName"
outfield6 = "Age"
outfield7 = "Description"
outfield8 = "HierarchyKey"
outfield9 = "ParagraphStyle"
outfield10 = "AreaFillRGB"
outfield11 = "GeoMaterialConfidence"
outfield12 = "DescriptionSourceID"

print "Adding " + featureclassin + "field map to. . ."
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

try:
	print "Appending data. . ."
	# Process: Append the feature classes into the empty feature class
	arcpy.Append_management(inFC, outFC, schemaType, fieldmappings, subtype)

except:
	# If an error occurred while running a tool print the messages
	print arcpy.GetMessages()

print "Append data to " + featureclassout + " " + " complete. . ."

