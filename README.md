# This is a repository for the MVP of a route generator 
This repository holds software for an application that converts a trail of gpx points stored in a .gpx file, into a readable route that lists street names, and turns taken based on the sequential order of the points recorded in the gpx file. 

### Overview of Features
- Runs locally 
- able to convert gpx points of a path to readable routes 
- Does not rely on any internal libraries to be installed (including python) 
- Easy to use front end GUI powered by flask 

### Errors, things to be Worked on 
- Does not handle u-turns well
- has minor road errors at certain intersections
- slow runtime (up to 10-12 minutes due to API calls) 

## User Manual 

### Basic Requirements 
- Computer running either Linux or Windows  (not tested on Mac) 
- Internet connection for calling the API
- Python 3
- Knowlege of how to build python files on the command line or in a text editor

### Starting the Application
If your computer doesn't have Python 3 currently installed, go to https://www.python.org/downloads/ and install the most recent version for your operating system.
To get started,
1. Download this repo
2. Build then run app.py
3. Open your web browser, type 127.0.0.1:5000 in the address bar, and then hit enter
 
### Entering Information
1. Once you're on the graphic interface, if you have a MapQuest API key, enter it into the textbox. If you leave this textbox empty and it doesn't work, click the link to be taken to the website to make a free account which will include a key.
2. Choose your .gpx file from the choose file button, then hit upload.

### Using the Application 
1. Once you click the "convert gpx to route" button a border should appear around the button which will go away when the conversion is complete.
2. Once the conversion is complete you can click the download button to download the route directions as a .csv file

## Developer's Manual 

### API Choice
The API could be swapped out for another by changing the parameters in the api_route.py file to match the parameters for input for the new API, along with changing the parsing process in that file to match the output of the new API.
