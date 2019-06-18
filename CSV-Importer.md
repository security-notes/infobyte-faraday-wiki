### Intro

The idea is to import an CSV file into Faraday's server uploading all the information into one of your workspaces.

### Index
* [CSV Format](#csv-format)
* [Command for Community version](#command-for-community-version)
* [Command for Commercial versions](#command-for-commercial-versions)
* [Sample File](#sample-file)

***

### CSV Format

The CSV file should have an special kind of formatting, so take in consideration the following rules:

**1)** The names of columns are:
* Host fields:
    * **host_name**
    * host_description
    * host_owned

* Services fields:
    * **service_name**
    * service_description
    * service_owned  #boolean
    * **service_port**
    * service_protocol
    * service_version
    * service_status

* Vulnerability fields:
    * **vulnerability_name**
    * **vulnerability_desc**
    * vulnerability_data
    * **vulnerability_severity**
    * vulnerability_refs
    * vulnerability_confirmed #boolean
    * vulnerability_resolution
    * vulnerability_status
    * vulnerability_policyviolations

* Vulnerability web fields:
    * **vulnerability_web_name**
    * **vulnerability_web_desc**
    * vulnerability_web_data
    * **vulnerability_web_severity**
    * vulnerability_web_refs
    * vulnerability_web_confirmed
    * vulnerability_web_status
    * vulnerability_web_website
    * vulnerability_web_request
    * vulnerability_web_response
    * vulnerability_web_method
    * vulnerability_web_pname
    * vulnerability_web_params
    * vulnerability_web_query
    * vulnerability_web_resolution
    * vulnerability_web_policyviolations
    * vulnerability_web_path
    * vulnerability_web_tagstags

_**Note:**_ those in **bold** are mandatory fields.

**2)** The following fields have a special format that you need to follow:

* Boolean (true or false):
    * host_owned
    * service_owned
    * vulnerability_confirmed
    * vulnerability_web_confirmed


* List (Values separated by comma):
    * service_port
    * vulnerability_refs
    * vulnerability_policyviolations
    * vulnerability_web_refs
    * vulnerability_web_policyviolations
    * vulnerability_web_tags

**3)** Possible values for vulnerability and vulnerability web SEVERITY:
* info
* low
* med
* high
* critical

**4)** Possible values for vulnerability and vulnerability web STATUS:
* opened
* closed
* re-opened
* risk-accepted

**5)** Possible values for service STATUS:
* open
* filtered
* close


**Warnings:** keep in mind the following concepts before importing an CSV file:

1) Hosts must ALWAYS have an interface associated.

2) Vulnerabilities must always have either a host OR a service associated to them.

3) Web Vulnerabilities must always be associated with a host AND a service.

4) Unicode chars not supported.

5) Anything not numeric entered on **service_port** will be ignored

### Command for Community version
~~~~
faraday-fplugin import_csv -u http://username:password@127.0.0.1:5985/ --csv /path/to/file/file.csv -w WORSKPACE_NAME
~~~~
_Options:_
 * --csv: the name and path of your CSV.
 * -w: Faraday's workspace where all the information will go to.


### Command for Commercial versions
~~~~
faraday-fplugin import_csv -u http://127.0.0.1:5985/ --csv /path/to/file/file.csv -w WORSKPACE_NAME --username USERNAME --password PASSWORD
~~~~

_Options:_
 * --csv: the name and path of your CSV.
 * -w: Faraday's workspace where all the information will go to.
 * --username: username of an Admin User.
 * --password: password of an Admin User.
 
### Sample file

Here you have an example file:

[file.csv](https://raw.githubusercontent.com/wiki/infobyte/faraday/files/file.csv)