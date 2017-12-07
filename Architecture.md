Faraday is composed by the Faraday Server and the Faraday Client with a Server 
Centric approach. The client talks almost exclusively with the server, and the 
server is used to syncronize the state of the program between instances.

For the moment, we use the popular No-SQL database CouchDB to provide a few
key features needed to improve your workflow, but we're working on replicating
those on Faraday Server to simplify the setup.

CouchDB Serves for the following purposes:

* Partial storage
* Notifications feed
* User management 

The server provides everything else using a REST API to make queries over 
sqlite DBs structured according to our Host/Services/Vulnerability model. Our
server acts as a web server build upon Twisted.

It is important to remember that, as said, CouchDB will totally be replaced by
our Faraday Server in the very near future. All this changes are transparent
to the user, nevertheless.

Server Centric approach
===
Every user connects to the same Faraday server, which is itself connected to a CouchDB database.
This permits seamless data sharing and syncronization.
![Sincronize_2](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Server-Comm.png)


Plugin Engine
=============
The following diagram explains the plugins architecture:
![Plugin_Controller](https://raw.github.com/wiki/infobyte/faraday/images/plugin_controller.png)

Plugin engine has the following components:

* Report Processor
* Plugin Controller
* Plugin Process
* Model Controller

The interaction of these components can be see in the following graph:

![Plugin Architecture](https://user-images.githubusercontent.com/568181/33733681-34e296ba-db69-11e7-94b8-8f3e9fda7a55.png)

Plugins, Report and Persistence Model each run in a separete Thread.
Communication between threads are made by queues.
Report Processor is a process and it could be one process for each workspace.

## Report Processor

Search for files in the .faraday/reports directory looking for external tools reports.
Report Processor will call the plugin controller using the method ProcessReport with the filename of the report.

## Plugin Controller

Plugin Controller will open the filename passed in the ProcessReport and will enqueue the contents in the output_queue.
The output_queue will be consumed by the Plugin Process

## Plugin Process

Plugin Process will detected the corresponding plugin that matchs the report file.
When it finds the plugin it will call the ProcessReport or ProcessOutput (if called from shell).
While the plguin is being executed in the Plugin Instance, methods like the CreateAndAddHost and similar will be called.
Each of the CreateAndADD (Or Update, Delete, etc) will enqueue an action code with an instance of persistence server models to the pending_actions queue.

## Model Controller

Model Controller consumes the pending_actions queue and will create http requests and serialize persistence model instances.
All http requests will be made to the faraday-server.