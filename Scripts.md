The scripts located at `$FARADAY/scripts/` are tools shipped with Faraday and refined to work seamlessly with it. Nevertheless, at their core, they are standalone tools totally capable of performing their function on their own. 

Faraday ships with three of these scripts:

* [Shodan Faraday](#shodan)
* [SSL Check](#sslcheck)
* [WCScan](#wcsan)

<a name="shodan"></a>
###Shodan Faraday

A command line tool to get information from Shodan located at `$FARADAY/scripts/shodan_faraday.py`. 

```
usage: shodan_faraday [-h] -q SHODAN_QUERY [-c COUNT] [-a SKEY]
                      [--faradayapi FARADAYAPI] [--debug DEBUG] [--version]
```

The following command will incorporate all the servers with Apache in Faraday

```
./shodan_faraday -q apache -a (SHODANKEY)
```

We provide a couple of wordlists to find specific queries using Shodan.
```
ls -lha $faraday/scripts/shodan_strings/
scada.txt
webcam.txt 
```

You can see an sample usage of these queries [in this video](https://www.youtube.com/watch?v=6_PM_jKkVNI)

###