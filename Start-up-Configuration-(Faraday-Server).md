# Intro

The Faraday Server is made to manage the CouchDB Database. This lets the user access all the information in one centralized platform, run periodic backups and make automated reports.

# Requirements

`# cd faraday`<br>
`/faraday# cat requirements_server.txt`

distribute==0.7.3<br>
python-docx==0.7.6<br>
six==1.9.0<br>
matplotlib==1.4.2<br>

# Start-up Configuration

To begin the initial setup, the user needs to run the executable **./setup_server.sh**

`/faraday# ./setup_server.sh`

![](https://raw.github.com/wiki/tartamar/faraday/images/faraday_setup_libraries.png)

`[+] Install required libraries? [y/N]`

* Install the necessary libraries to execute the application.These can be found in the folder, requirements_server.txt.

`[+] Install backup crontab? [y/N]`

* Install a batch process to run periodic backups of the database.

`[+] Install Report Generation crontab? [y/N]`

* Install a batch process to make automated reports.

`[+] Faraday server is full configured`


# Restore the Couchdb user administrator

It is possible to restore the database´s users using the following script:

/faraday# ./reset_admin_couchdb.sh

Tincho tenés un errorcito de ortagrafía dice ¨dase¨en vez de ¨base¨. :)

`/faraday# ./reset_admin_couchdb.sh`

**Important: The process will eliminate existing users**
