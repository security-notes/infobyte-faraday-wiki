This plugin is a script developed in JRuby as a extender to the Burp Proxy API (Pro/Community).

#Dependencies:    
Jruby 1.7.6 Complete [[http://www.jruby.org/download]]

#Configuration:
1) (Burp) In the Extender Tab, Options, in the Ruby Enviroment option set to the PATH of jruby-complete.jar  
2) (Faraday) Edit the RPCSERVER of faraday/plugins/repo/burp/faraday-burp.rb to the IP and Port of Faraday's RPC  

    #FARADAY CONF:
    RPCSERVER="http://127.0.0.1:9876/"

3) (Burp) Inside the extensions, select Ruby Extension and set the location of faraday-burp.rb, normally faraday/plugins/repo/burp/faraday-burp.rb  

#Notes
By default, this plugins adds the vulnerabilities already created at Burp, new vulnerabilities are added in a interactive way.
Change the following variable in faraday-burp.rb  
    IMPORTVULN=1 #1 if you like to import the current vulnerabilities, or 0 if you only want to import new vulns

#Bugs
If you export a Scanner XML file from Burp, you must select "Base64-encode" option. If not the exported XML file will be corrupt due lack of escaping html characters