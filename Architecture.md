Faraday is composed by the Faraday Server and the Faraday Client with a Server 
Centric approach. The client talks almost exclusively with the server, and the 
server is used to syncronize the state of the program between instances.

Faraday uses SQLAlchemy to map objects to relational databases. We support and recommend PostgreSQL as a database engine.

The server provides everything else using a REST API. You can also make queries over
the relational databse structured according to our Host/Services/Vulnerability models (server/models.py). Our
server acts as a web server build upon Twisted which provides websockets, wsgi and serves static files.


## Server Centric approach

Every user connects to the same Faraday server, which is itself connected to a PostgreSQL database.
This permits seamless data sharing and syncronization.
![Sincronize_2](https://user-images.githubusercontent.com/568181/33737838-42252c90-db76-11e7-9d04-fb27afcb03bb.png)


## Plugin Engine

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

### Report Processor

Search for files in the .faraday/reports directory looking for external tools reports.
Report Processor will call the plugin controller using the method ProcessReport with the filename of the report.

### Plugin Controller

Plugin Controller will open the filename passed in the ProcessReport and will enqueue the contents in the output_queue.
The output_queue will be consumed by the Plugin Process

### Plugin Process

Plugin Process will detected the corresponding plugin that matchs the report file.
When it finds the plugin it will call the ProcessReport or ProcessOutput (if called from shell).
While the plguin is being executed in the Plugin Instance, methods like the CreateAndAddHost and similar will be called.
Each of the CreateAndADD (Or Update, Delete, etc) will enqueue an action code with an instance of persistence server models to the pending_actions queue.

### Model Controller

Model Controller consumes the pending_actions queue and will create http requests and serialize persistence model instances.
All http requests will be made to the faraday-server.