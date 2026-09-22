**Identifying At-Risk Public Schools Near Flood-Hazard Areas in the Texas Golden Triangle**

--------

**Project Overview**



This project identifies public schools that are located within or near FEMA-designated Special Flood Hazard Areas in the Texas Golden Triangle. The analysis area is focused around Jefferson, Hardin, and Orange Counties in Southeast Texas.



This project was created using Python and Arcpy that incorporates an interactive workflow. The analysis allows a user to select one of the three analyzed counties and a flood-zone buffer distance. The script will then generate flood-hazard data as well as a list of public schools that fall into the analysis area.

---------

**Study Area**



The study area used in this project are the three counties that consist of the Golden Triangle in Southeast Texas:

  * Jefferson County

  * Hardin County

  * Orange County

Here is a map of the overall study area:
![Study Area](images/study_area.png)

--------

**Project Objectives**



The objectives of this project were to:

  * Create a workflow using Python-based GIS that is interactive.

  * Allows the user to select the study area (County selection).

  * Identify and select the FEMA Flood Hazard Areas within the user-selected County.

  * Allows the user to specify a buffer distance around the selected flood-hazard areas.

  * The analysis will then select regular school institutions within the specified study area.

  * Outcome produces working GIS layers and a school list meeting the selected criteria.

--------

**Tools and Technology**

  * Python

  * ArcPy

  * ArcGIS Pro

  * Jupyter Notebook

  * Texas public school data

  * FEMA flood-hazard data

--------

**Analysis Workflow**



The following steps were used to perform the analysis:

  1. The user performs a selection of either Jefferson, Hardin, or Orange County.

  2. An extraction is performed to obtain the county-boundary data.

  3. The county layer is then projected to NAD 1983 UTM Zone 15N.

  4. The appropriate flood-hazard data is then selected.

  5. Flood-hazard polygons are then clipped to the selected county polygon.

  6. The specified FEMA flood-hazard areas are then selected.

  7. The selected flood-hazard polygons are then dissolved.

  8. The user is then prompted to specify a buffer distance in miles. There is an option to use 0.

  9. Regular, public school institutions are then selected within the specified County.

  10. The schools that intersect the flood-hazard zones are identified.

  11. A report is then made that lists out the schools that meet the analysis criteria.

--------

**Results**



This is an image of the results shown for an analysis of Orange County.



![Orange County Flood Risk Results](images/orange_county_results.png)



This output identified public school institutions that were within the flood-hazard area or those that fell within the buffer distance defined. The analysis can be adjusted depending on the user-defined buffer distance proximity.

--------

**Python Implementation**



The project is separated into two working parts. A Jupyter Notebook and a Python module.



The main analysis, geoprocessing operations, and user input is controlled using the main notebook.



The Python module contains all of the functions used in the analysis.



The entirety of the project code is available for perusal and use in the **code** directory.

--------

**Data Sources**



The datasets used in analysis:

  * FEMA flood-hazard data

  * Texas public-school location data

  * Texas county-boundary data



The actual datasets used in analysis were not included here. The contents of this project include only the Python workflow, project documents, and an example of output analysis run by the program.

---------

**Full Project**



The full project report can be perused. This report is located within the **docs** directory.

---------

**Repository Layout**



golden-triangle-flood-risk

  * code/

    * term\_project\_notebook.ipynb

    * term\_project\_module.py

  * images/

    * study\_area.png

    * orange\_county\_results.png

  * docs/

    * flood\_risk\_project\_report.pdf

  * README.md

--------

**Project Context**



This project was completed during graduate-level courses during my tenure at the University of Oklahoma while pursuing a Master of Science in Geospatial Technologies. This project incorporates the use of Python and Arcpy to automate user-defined GIS analysis.

