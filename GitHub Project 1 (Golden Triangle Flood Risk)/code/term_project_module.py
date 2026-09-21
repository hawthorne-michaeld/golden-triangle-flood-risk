###----------------------------
# Michael Hawthorne (Term Project Module)
# Title:
# Identifying Public Schools Near Flood-Hazard Areas in the Texas Golden Triangle
#
# This module is used in conjunction with a main Jupyter Notebook file to analyze and select valid schools
# that are within a user defined distance from FEMA flood hazard areas within the Texas Golden Triangle

###----------------------------

# imports:
import arcpy

#-------------------------
# county selection: (while loop 1)(conditional for county and source)
def input_county_choice(): # defines the county input choice module

    valid_counties = ["Jefferson", "Hardin", "Orange"] # The valid 3 choices for counties
    # User input for county selection. .title() is a good way to keep the selection not case sensitive
    county = input("Please type either 'Jefferson', 'Hardin', or 'Orange' to choose your county: ").strip().title()
    # while loop for invalid county selections
    while county not in valid_counties:
        print("You have chosen an Invalid County Selection.")
        # prompts the user again for the proper county selection
        county = input("Please type either 'Jefferson', 'Hardin', or 'Orange': ").strip().title()
    # returns the valid county selection to the main script
    return county

# county selection continued:
def county_selection(county_layer, county_name, output_layer): # defines the county selection module
    # searches for the user designated county in the county layer
    county_search = f"CNTY_NM = '{county_name}'"
    # uses the select tool to choose the proper county information
    arcpy.analysis.Select(county_layer, output_layer, county_search)
    # returns county selection to the main script
    return output_layer

#-------------------------
# projection: (NAD 1983 UTM Zone 15N)
def projection_layer(projection_input, projection_output): # defines the projection module
    # sets the output coordinate system to the proper spatial reference for Southeast Texas
    coordinate_system = arcpy.SpatialReference("NAD 1983 UTM Zone 15N")
    # uses the project tool to project the proper coordinate system
    arcpy.management.Project(projection_input, projection_output, coordinate_system)
    # returns the projection to the main script
    return projection_output

#-------------------------
# flood zone selection: (conditional statement)
def flood_zone(county_name, jefferson_fldzone, state_flood): # defines the flood_zone selection module
    # The jefferson flood zone information is separate from the State flood information. Jefferson county,
    # is not included in the regular, state flood zone dataset
    if county_name == "Jefferson": # special 'if' statement for Jefferson county
        flood_layer = jefferson_fldzone
    else:
        flood_layer = state_flood
        # sets the flood zone layer to state flood zone layer if Jefferson county is not selected
    # returns the proper flood zone layer to the main script
    return flood_layer

# flood zone clipping:
# This will clip the state flood polygons to the county of choice (Hardin, Orange)
def flood_zone_clip(county_name, flood_layer, county_layer, output_layer):
    # defines flood zone clip module
    # no reason to clip if the selection choice is 'Jefferson county'
    if county_name == "Jefferson":
        # returns the selection to the main notebook
        return flood_layer
    # clip the flood zones from the state layer for Hardin and Orange counties
    else:
        arcpy.analysis.Clip(flood_layer, county_layer, output_layer)
        # returns the selection to the main notebook
        return output_layer

# Selects only those areas that are considered FEMA Special Flood Hazard Areas
def sfha_selection(flood_layer, output_layer):
    # selects only those polygons that are set to 'True' for Special Flood Hazard Areas
    sfha_search = "SFHA_TF = 'T'"
    # uses the analysis select tool to select those SFHA polygons
    arcpy.analysis.Select(flood_layer, output_layer, sfha_search)
    # returns the output selection to the main notebook
    return output_layer

# flood zone dissolve module:
# defines the dissolve flood zone module
def dissolve_flood_zone(input_layer, output_layer):
    # uses the dissolve tool to dissolve the selected SFHA polygons
    arcpy.management.Dissolve(input_layer, output_layer)
    # returns dissolved selection to main notebook
    return output_layer

#-------------------------
# flood buffer/proximity: (while loop 2)(conditional for buffer)
# defines the buffer distance module
def input_buffer_distance():

    # prompts the user to input a buffer distance as a float:
    buffer_distance = float(input(
        "Enter a buffer distance number (in miles) from the flood zone: "
        "Entering a value of '0' will include all schools that are directly in a flood zone: "))
        # makes it to where you can just select all schools that are just the selected flood zone area
    # while loop to prevent negative input values:
    while buffer_distance < 0:
        print("Input buffer distance cannot be a negative distance.")
        # prompts the user again to enter either 0 or a positive number as a float:
        buffer_distance = float(input(
            "Enter either '0' or a number greater than 0 for the buffer distance selection: "))
    print("Please wait on your selection output.")
    # because the prompts can be a little slow to return, tells the user to wait patiently for next prompt

    # returns the buffer distance value to the notebook
    return buffer_distance

# buffer module:
# defines the actual flood buffer module (not just the distance input)
def flood_buffer(flood_layer, buffer_distance, output_layer):

    # If the buffer selection is greater than 0, then there is a buffer output:
    if buffer_distance > 0:
        # sets the buffer distance to miles
        distance = f"{buffer_distance} Miles"
        # runs the buffer analysis tool from user input information
        arcpy.analysis.Buffer(flood_layer, output_layer, distance)

        # returns the buffer output to the notebook
        return output_layer
    # When '0' is entered, this selects the flood zone polygons to use for analysis instead
    else:
        return flood_layer

#-------------------------
# school selection:
# module that selects regular, instructional schools in the county of choice
def school_selection(school_layer, county_name, output_layer):
    # sets the county value to the appropriate county chosen
    county_value = f"{county_name} County"
    # chooses the schools based on the county and instruction type in the school layer
    school_search = (f"Subregion = '{county_value}' AND "f"USER_instr = 'REGULAR INSTRUCTIONAL'")
    # uses the select analysis tool to select the schools that meet this criteria
    arcpy.analysis.Select(school_layer, output_layer, school_search)
    # returns the chosen schools to the notebook
    return output_layer

#-------------------------
# determine at risk schools: (selects all schools that fall within the user specified criteria)
# defines the at risk schools module
def at_risk_schools(school_layer, flood_analysis_area, output_layer):

    # makes a school feature layer for the analysis
    arcpy.management.MakeFeatureLayer(school_layer, "school_layer")

    # uses the select layer by location tool and 'intersect' as the relationship value
    arcpy.management.SelectLayerByLocation("school_layer", "INTERSECT", flood_analysis_area)

    # saves the selected at-risk schools in a new layer using 'CopyFeatures'
    arcpy.management.CopyFeatures("school_layer", output_layer)

    # returns the selected schools to the notebook
    return output_layer

# determines the count of at-risk schools: (just to get a number output of the selected schools)
# defines the school count module
def school_count(school_layer):

    # uses 'GetCount' to get the number of selected schools
    count = int(arcpy.management.GetCount(school_layer)[0])

    # returns the count value to the notebook
    return count
