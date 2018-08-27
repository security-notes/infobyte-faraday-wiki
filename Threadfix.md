Steps to follow:
1) Download json report
To export the threadfix json file use the following url:

http://localhost:5985/_api/v2/ws/demo_workspace/vulns-threadfix

This will download a json file of the workspace in the url

2) Configure threadfix new scanner

Then configure threadfix and add a new “Faraday” Scanner:

https://denimgroup.atlassian.net/wiki/spaces/TDOC/pages/461504516/Create+a+New+Scanner

3) Import the json file to threadfix as a new scan using the “Faraday” scanner.
