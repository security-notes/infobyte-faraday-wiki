## Searcher script
In order to search specific objects inside your Faraday workspace and execute several actions over them, we created **Searcher**. This tool has some options which can be printed with the following command:

    $ ./searcher.py -h
    usage: searcher.py [-h] -w WORKSPACE [-s SERVER] [-u USER] [-p PASSWORD]  [-o OUTPUT] [-l LOG]
    Search duplicated objects on Faraday
    optional arguments:
    -h, --help            show this help message and exit
    -w WORKSPACE, --workspace WORKSPACE Search duplicated objects into this workspace
    -s SERVER, --server SERVER server
    -u USER, --user USER Faraday user
    -p PASSWORD, --password PASSWORD Faraday password
    -o OUTPUT, --output OUTPUT Choose a custom output directory
    -l LOG, --log LOG     Choose a custom log level


## How does it work?
**Searcher** needs a rule list to be used, these rules determine concepts such as _specific object to select_ and _actions that will be executed_ if some conditions are met inside the current Faraday workspace.
Basically, a rule has a structure like this:

    [OBJECT]
    [IF]
    [THEN]

With this in mind, we use this global structure of rule:


    {
        ‘id’: ‘CU1’,
        
        ‘model’:’Vulnerability’,
        ‘parent’: ‘192.168.42.55’OBJECT
        ‘fields’:[‘name’,’desc’,’description’]
        ‘object’:’creator=Nmap ref=nmap-10’,

        ‘conditions’:[“refs=nessus-333”,”name=smb-vuln-056”], IF

        ‘actions’:[“--UPDATE:confirmed=True”]THEN
    }


Where the fields 'model', 'parent', 'fields' and 'object' allow to get the object that will be processed, and conditions field tells us when the actions can be executed.

### Rule description

Each rule has optional and mandatory fields, it depends on our purpose:

|  			Field 		      |  			Description 		                                                                                                                                                                                                                      |  			Mandatory 		 |  			Examples 		                                                                                                                                                                               |  			Allowed values 		               |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
|  			id 		         |  			Rule identifier, must be unique 		                                                                                                                                                                                                  |  			Yes 		       |  			R1 		                                                                                                                                                                                     |  			  			 		                           |
|  			model 		      |  			Allows determinate which model select 		                                                                                                                                                                                            |  			Yes 		       |  			  			 		                                                                                                                                                                                     |  			Vulnerability, Host, 			Service 		 |
|  			parent 		     |  			It works like a scope, we are going to search contained models 			into it, if isn’t specified, we are going to search models in 			the whole workspace, also it can be set with a services or host 			properties like name or Identifier. 		 |  			No 		        |  			192.168.42.55, 			http, 			  			 		                                                                                                                                                                |  			  			 		                           |
|  			fields 		     |  			Allows to compare using similarity between two model’s name, 			with this element we can determine if these objects has similar 			names and then select one to apply the actions 		                                                      |  			No 		        |  			[‘name’, ‘description’, 			‘desc’, ‘confirmed’] 		                                                                                                                                           |  			Model’s fields  			 		             |
|  			object 		     |  			Allows know exactly what object should be 			to process, it has an specific format , also we can set it with a 			regex by name, in that way we have more options and a selecting  			generic process. 		                                    |  			Yes 		       |  			creator=Nmap 			confirmed=True 			regex=error$ 			name=OS%Config 		                                                                                                                                |  			Model’s fields 		               |
|  			conditions 		 |  			The conditions help us to decide if the actions can be executed 			or no, it are a list of matching between keys an values of current 			model, if each conditions are met, the action will run. 		                                       |  			No 		        |  			refs=nessus-333 			name=smb-vul-056 		                                                                                                                                                       |  			Specific format 		              |
|  			actions 		    |  			The actions are the response that 			each rule gives having account the desire goal. There are 4 kinds 			of actions: 			UPDATE, ALERT, DELETE and EXECUTE, these will be explained 			later 		                                                 |  			Yes 		       |  			--UPDATE:severity=critical 			--UPDATE:confirmed=True 			--UPDATE:refs=nessus-333 			--UPDATE:-refs=nmap-10 			--UPDATE:template=tempId 			--ALERT:test@gmail.com 			--EXECUTE:/create_task.sh 			--DELETE: 		 |  			Specific format 		              |



### Usage examples

To use Searcher tool, we must keep in mind some elements to specify such as current workspace.

    $ ./searcher.py –w=my_workspace –s=http://127.0.0.1:5984 –u=faraday –p=changeme
    $ ./searcher.py –w=my_workspace (Community version)

**Mandatory:** Faraday's user and password. These elements could be omitted if we are using the Community version.



## Rules configurations examples

 1- We are going to change the severity to "critical" and the confirmed status to True on all the vulnerabilities whose names begin with ‘Device’ and parent is ’50.56.220.123’. The conditions to make this change is that there should be another vulnerability with severity "info" in this same host and another vulnerability which creator is Nessus and its name begin with ‘OS’:

    {
        'id': 'CLIENT_TEST_3',
        'model': 'Vulnerability',
        'parent': '320131ea90e3986c8221291c683d6d19bfe8503b',
        'object': "creator=Nessus --old",
        'conditions': ["severity=info", "creator=Nessus"],
        'actions': ["--UPDATE:refs=VCritical", "--UPDATE:confirmed=True"]
    }

 2- In this example we are adding the item VCritical to older vulnerability’s refs field with creator Nessus, also set its confirmed value to True if in its parent with id '320131ea90e3986c8221291c683d6d19bfe8503b' exists another vulnerability with severity "info" and creator Nessus.

    {
        'id': 'CU3A',
        'model': 'Vulnerability',
        'fields': ['name'],
        'actions': ["--UPDATE:confirmed=False"]
    }

 3- With this rule we can search pairs of similar vulnerabilities by name inside a same level and then to confirm the more recent of them, Ex ‘Auth error’ and ‘Auth error 2’

 4- This rule is similar to example 3, just we are going to select the older vulnerability from current pair.

    {
        'id': 'CU3B',
        'model': 'Vulnerability',
        'fields': ['name'],
        'object': "--old",
        'actions': ["--UPDATE:confirmed=True"]    
    }

 5- We are going to apply the template “EN-Cifrado Debil (SSL weak ciphers)” to all vulnerabilities with name = “OS Identification”.

    {
            'id': 'CU5B',
            'model': 'Vulnerability',
            'object': " name=OS%Identification",
            'actions': ["--UPDATE:template=EN-Cifrado Debil (SSL weak ciphers)"]
    }

 6- We can remove all services with name “http” from the workspace


