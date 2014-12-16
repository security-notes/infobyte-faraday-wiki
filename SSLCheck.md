## # SSLCheck

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_qt.png)

Also, we added a plugin for Faraday that is a tool to verify SSL/TLS errors for remote hosts.A Python script using code from OpenSSL, lets a user check the SSL/TLS remote server. The potential vulnerabilities (or the real ones) showup in red on the analysis report, that one can easily export to XML format.

Follow the steps below:

1. Open Faraday using the following command: ./faraday.py --dev-mode, so that it refreshes the plugins folder

2. Now that you Faraday open, go to scripts folder (cd scripts)

3. Execute the command ./sslcheck.py target (./sslcheck.py 192.168.10.254)

Also, you can quickly run  the comand for several targets and domains, the targets need to be written seperately with a single space.

./sslcheck.py 192.168.10.254 facebook.com www.google.com 192.168.10.168