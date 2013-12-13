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
Change the variable **IMPORTVULN** in faraday-burp.rb if you only want to import new vulns

    IMPORTVULN=0
