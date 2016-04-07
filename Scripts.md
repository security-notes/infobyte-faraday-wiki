The scripts located at `$FARADAY/scripts/` are tools shipped with Faraday and refined to work seamlessly with it. Nevertheless, at their core, they are standalone tools totally capable of performing their function on their own. 

Faraday ships with two of these scripts:

* [Shodan Faraday](#shodan)
* [SSL Check](#sslcheck)

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

<a name="sslcheck"></a>
### SSL Check

Located at `$FARADAY/scripts/sslcheck.py`, SSL Check is a tool to verify SSL/TLS errors in remote hosts. With code from OpenSSL, this scripts lets a user check the SSL/TLS remote server. The potential vulnerabilities appear in red on the analysis report, which can be easily exported to XML. 

As noted above, the preferred way of using theses scripts is with Faraday, although it is not necessary. To run the script from Faraday, just open the program, cd to the scripts folders and run 

```
./sslcheck.py TARGET1 TARGE2 TARGET3 ...
```

For example: ```./sslcheck.py 192.168.10.254 google.com 192.168.5.210 facebook.com ```

<a name="wcscan"></a>