Faraday is composed of the Faraday Server and the Faraday Client with a Server-Centric approach. The Client talks almost exclusively with the Server, and the Server is used to synchronize the state of the program between instances.

Execute:
```
faraday-manage database-schema
```
For an image explaining the schema of our database.

Faraday uses PostgreSQL as a database engine.

The Server provides everything else using a REST API. You can also make queries over
the relational database structured according to our Host/Services/Vulnerability models (server/models.py). Our
Server acts as a Web Server build upon Twisted which provides websockets, wsgi and serves static files.

## Server Centric approach

Every user connects to the same Faraday Server, which is itself connected to a PostgreSQL database.
This permits seamless data sharing and synchronization.
![Sincronize_2](https://raw.github.com/wiki/infobyte/faraday/images/architecture/faraday_schema.png)


## Plugin Engine

The following diagram explains the plugins' architecture:
![Plugin_Controller](https://raw.github.com/wiki/infobyte/faraday/images/architecture/plugin_controller.png)

Plugin engine has the following components:

* Report Processor
* Plugin Controller
* Plugin Process
* Model Controller

The interaction of these components can be seen in the following graph:

![Plugin Architecture](https://raw.github.com/wiki/infobyte/faraday/images/architecture/plugin_architecture.png)

Plugins, Report and Persistence Model each run in a separate Thread. Communication between threads are made by queues. Report Processor is a process and it could be one process for each workspace.

### Report Processor

Search for files in the .faraday/reports directory looking for external tools reports.
Report Processor will call the plugin controller using the method ProcessReport with the filename of the report.

### Plugin Controller

Plugin Controller will open the filename passed in the ProcessReport and will enqueue the contents in the output_queue.
The output_queue will be consumed by the Plugin Process

### Plugin Process

Plugin Process will detect the corresponding plugin that matches the report file.
When it finds the plugin it will call the ProcessReport or ProcessOutput (if called from shell).
While the plugin is being executed in the Plugin Instance, methods like the CreateAndAddHost and similar will be called.
Each of the CreateAndADD (Or Update, Delete, etc) will enqueue an action code with an instance of persistence server models to the pending_actions queue.

### Model Controller

Model Controller consumes the pending_actions queue and will create http requests and serialize persistence model instances.
All http requests will be made to the faraday-server.
