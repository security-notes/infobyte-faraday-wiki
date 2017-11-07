The idea is to import an CSV file into Faraday's server uploading all the information into one of your workspaces.

The CSV file should have an special kind of formatting...

First of all:

The names of columns are:

* Host fields:
    * **host_name**
    * host_description
    * host_owned
    * host_os

* Interface fields:
    * **interface_name**
    * interface_description
    * interface_hostnames
    * interface_mac
    * interface_network_segment
    * interface_ipv4_address
    * interface_ipv4_gateway
    * interface_ipv4_mask
    * interface_ipv4_dns
    * interface_ipv6_address
    * interface_ipv6_gateway
    * interface_ipv6_prefix
    * interface_ipv6_dns

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
    * vulnerability_web_tags

(**mandatory fields**)

The following columns names have a special format that you need to follow.

* Boolean (true or false):
    * host_owned
    * service_owned
    * vulnerability_confirmed
    * vulnerability_web_confirmed


* List (Values separated by comma):
    * interface_hostnames
    * service_port
    * vulnerability_refs
    * vulnerability_policyviolations
    * vulnerability_web_refs
    * vulnerability_web_policyviolations
    * vulnerability_web_tags

Possible values for vulnerability and vulnerability web SEVERITY:
* info
* low
* med
* high
* critical

Possible values for vulnerability and vulnerability web STATUS:
* opened
* closed
* re-opened
* risk-accepted

Possible values for service STATUS:
* open
* filtered
* close

WARNINGS:
1) Unicode chars not supported.
2) host_name not can be empty.
3) Anything not numeric entered on Port will be ignored

A few important concepts you should keep in mind before importing an csv file:

1) Hosts must ALWAYS have a interface associated.

2) Vulnerabilities must always have either a host OR a service associated to them.

3) Web Vulnerabilities must always be associated with BOTH a host AND a service.




Command for Community:
~~~~
python2 ./bin/fplugin import_csv -u http://username:password@127.0.0.1:5985/ --csv /path/to/file/file.csv -w WORSKPACE_NAME
~~~~

 --csv The name and path of your csv.

 -w Faraday's workspace where all the information will go to.


Command for Commercial Versions:
~~~~
python2 ./bin/fplugin import_csv -u http://127.0.0.1:5985/ --csv /path/to/file/file.csv -w WORSKPACE_NAME --username USERNAME --password PASSWORD
~~~~

 --csv The name and path of your csv.

 -w Faraday's workspace where all the information will go to.

 --username  Username of an Admin User.
 --password  Password of an Admin User.
 
Here you have an file example:

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/files/file.csv)