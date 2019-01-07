# app-iReporter

[![Build Status](https://travis-ci.com/Anguandia/app-iReporter.svg?branch=develop)](https://travis-ci.com/Anguandia/app-iReporter)
[![Coverage Status](https://coveralls.io/repos/github/Anguandia/app-iReporter/badge.svg)](https://coveralls.io/github/Anguandia/app-iReporter)
[![Maintainability](https://api.codeclimate.com/v1/badges/7405228269881aa69536/maintainability)](https://codeclimate.com/github/Anguandia/app-iReporter/maintainability)

### INTRODUCTION

This is the server side implementation of an online events logging system meant to work with any user interface that will communicate through JSON.

The complete application will provide a platform for any cncerned citizens to flag incidences of public concern to the attention of the concerned authorities, bodies and the general public in two categories; 
corruption incidences coined as **red flags** and occurences that need intervention such as natural disasters, security threats, ailing public infrustructure, pandemics, and any other issues of public concern, collectively termed as **intervention reports** herin.

This current phase of the prject however focuses on modelling the red flags component of the entire application

### FEATURES AND OPERATIONS

The current application takes in client report data to produce and store report records that can the be retrieved, some fields updated and records deleted. Details in Details section

##### *Operations summary*

The following operations are provided for in the current version of the application:
- Create a red flag record
- Get all red flags
- Get a given red flag by id
- Update either of the location, status, or comment of a particular red flag selected by id
- Delete a given red flag nselected by id

##### *Error handling:*
Rigorous checks against the followin errors with appropriate responses as detailed in the [documentation](https://app.swaggerhub.com/apis/Anguandia/default-title/1):
- Creating duplicate records
- Invoking wrong actions for valid routes
- Wrong/invalid URLs
- Wrong/invalid request data
- Requests to operate on non existent records
- Empty/wrong format intput where input is required

##### *Scope*

The application has no user component, authentication or authorization in this version but provides for full manipulation of records

##### *User experience:*

User experience is at the core of the design.The application furnishes informative responses to every request, pointing out possible errors in requests if not executed.
responses are of two general categories; request success feedback and error responses, each producing the response code, requested resource (if required and successful) and the appropriate response message

### URLs AND API VERSIONING

The URLs are of the general format protocol://domain/version-prefix/path
- Protocol: https for cloud hosting and http for local hosting
- domain: fast-ravine-44023.herokuapp.com cloud hosting and localhost:port=5000 default for localhost
- version-prefix: api/v1. Version is v1 for current api, subsequent api's will be versioned as v2, v3, etc
- path: resource/red_flag_id/endpoint
  where:
  - resource is red_flags for current version, subsequent api's will include 'intervention_records' and 'users' resources
  - id an integer specifying the particular resource for a given operation. Used to identify a resource for a delete, update or get-one operation. Depending on the user interface, may have to be supplied explicitly in the URL
  - endpoint: Specifies one of the record's properties of 'location', 'comment' and 'status' for update operations. Depending on user interface, may have to be explicitly supplied in the URL.
  Endpoint also specifies delete for a delete action on the specified record
  
##### *Summary of valid URL paths*
  - /api/v1/red_flags: create a red flag or get all red flags
  - /api/v1/red_flags/red_flag_id: get or delete red flag specified by red_flag_id
  - /api/v1/red_flags/red_flag_id/endpoint: update property endpoint of red flag specified by red_flag_id or if endpoint is delete, delete selected red flag 
   
### DETAILS
##### *Create red-flag:*

    URL-PATH: /red_flags

    Method: POST
    
    Request body:

    The request body MUST contain values for red-flag properties of location, comment, and createdBy.
     location: name of the place of occurrence of the alert event, can not be only integers, must be descriptive
     comment: description of the event being reported, must be descriptive, can be detailed
     createdBy: Identity of the user raising the alert.
     title: a one-line summary of the incident
   
    Responses:
  
     If any of errors, a corresponding response will be returned. Else, the record is created.
     Additional attributes are filled with defaults and success response message returned.
     Of the remaining attributes, type, image and video can be explicitly supplied.
     The remaining, id, createdOn and status are system generated
 
##### *Get all red flags:*

    URL-PATH: protocal://domain/api/v1/red_flags
  
    Method: GET
  
    Responses:
  
    This fetches and returns an array of all records along if any record() else an empty array

##### *Get individual record:*

    URL-PATH: /red_flags/<red_flag_id>. red_flag_id must be an integer
  
    Method: GET
  
    Responses:
  
    With an integer id of an existing record, returns single element array of the given record
    If non existent, an empty array
    Else if error in red_flag_id or resource name, returns appropriate error message
  
##### *Edit a given record:*

    URL-PATH: /red_flags/<red_flag_id>/<property>
 
    Method: PATCH
  
    Request body:
  
    The location value fore edit must be a string.
    Format: latitude,longitude
    
    Action and responses
    
    Updates the specified attribute of the record with the given id.
    Editing the status or comment of a record will overwrite current values with the supplied values.
    Updating the location will append coordinates to location or overwrite existing coordinates. 
    Any errors will invoke appropriate responses
  
##### *Delete a given record:*

    URL-PATH: /red_flags/<id>/delete
 
    Method: DELETE
  
    Responses:
  
    If record with given id exists, request will delete the record and return a 'record deleted' message in the 
    response, else it will return record not  found message
  
##### *Usage info:*

    URL: protocol://domain/version-prefix/

    This base(default) root displays a simple user guide

### ACCESS:

  This product, code and documentation can be accessed through the cloud links provided in the [links and related information section](PRODUCT LINKS AND RELATED INFORMATION) or locally when installed

### TECHNOLOGIES USED

  - Python language
  - Flask framework

### INSTALLATION

 ##### *Preparation:*

- If not yet done, install a suitable version of python 3.7 onward for your operating system [here](https://www.python.org/downloads/) or from any source
- If using a windows system, install a suitable version of [git client](https://git-scm.com/downloads) for your system 

##### *Clone the repo:*

- Open your editor and navigate to your preferred location for the app
- Clone the api with the `git clone https://github.com/Anguandia/app-iReporter` command

##### *Setup and activate your virtual environment:*

- Navigate to the cloned project directory with `cd app-iReporter` command
- Run `virtualenv name` to setup a virtual environment, name is the name you choose for your virtual environment.
- Run `source name/Scripts/activate` for windows else `name/bin/activate` to activate your virtual environment

##### *Install project dependencies*
- Run `pip install -r requirements.txt` from the root folder to install all dependencies
The application is successfully installed, you can proceed to run the application. If you need to deactivate the virtual environment, run the `deactivate` command from any directory

### RUNNING THE APPLICATION
- Run the command `python run.py` from the root directory or
- Run the commands `export FLASK_APP=run.py` and `flask run` or in your root directory, create a .evn file with the command `touch .env`
- In the .env file, save the lines `export FLASK_APP=run.py` and the command for activating the virtual environment.
- If you have the .env file, you can always run the app with the `flask run` command and do not need to manually activate the virtual environment because autoenv is among the packages you installed with the pip -r ... command earlier, it will always activate the environment whenever you cd
- The application is now running on localhost, copy the URL displayed in your terminal where the app is running and proceed to making requests and exploring the application

### USING AND EXPLORING THE APPLICATION

Thurs far, no user interface has been developed for the application, hence it can be accessed through a number of http clients like cURL, postman, HTTPie, etc. cURL and HTTPie are command line clients while postman is a GUI client. Attention is given here to postman, but feel free to explore other options

##### **Set up the http client**

*cURL and HTTPie:* Checkout [cURL](https://curl.haxx.se/docs/manpage.html) and [HTTPie](https://httpie.org/) installation documentation and usage or from any suitable sources

*postman:* Download and install postman [here](https://www.getpostman.com/downloads/).

##### Making requests with postman
- In the main view pane, click on `headers` and enter the key `content-type` and value `application/json`
- In the address bar enter the URL for the request you want to make, see Features for reference.
- Select the method from button left of address bar
- If a post/patch request, click on body and select the raw radio
- Enter your request data in a json dictionary of format {"key": "value"}
- Hit send and wait for the response

### ACKNOWLEDGEMENTS:
A great deal of indebtedness to Andela Uganda for providing not only an opportunity to explore and exploit talent, but also the environment, resources and nurturing

A lot of contribution and mentoring from the learning facilitators at the Andela Level-up program is plainly unequaled in the realization of this product to this stage, especially the patience and understanding the facilitators unceasingly exercised

### PRODUCT LINKS AND RELATED INFORMATION

Code on github: [https://github.com/Anguandia/app-ireporter]

Heroku link: [https://fast-ravine-44023.herokuapp.com/]

Pivotal tracker: [https://www.pivotaltracker.com/n/projects/2232384] Contains the project plan, implementation and management details

Documentation: [https://app.swaggerhub.com/apis/Anguandia/default-title/1#] Technical documentation of application detailing usage, parameters, expected behavior, requests and responses, etc.

Licencing: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
