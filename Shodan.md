It is a command line tool to get information from shodan

You can find the script in $faraday/scripts/shodan_faraday.py

usage: shodan_faraday [-h] -q SHODAN_QUERY [-c COUNT] [-a SKEY]
                      [--faradayapi FARADAYAPI] [--debug DEBUG] [--version]

The following command will incorporate all the server with apache in Faraday

./shodan_faraday -q apache -a (SHODANKEY)

We have create some wordlist to find specify stuff using shodan
```
ls -lha $faraday/scripts/shodan_strings/
scada.txt
webcam.txt 
```
In the following video you can see an example using this queries:
https://www.youtube.com/watch?v=6_PM_jKkVNI