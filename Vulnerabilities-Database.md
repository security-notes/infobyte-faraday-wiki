Find yourself writing the same descriptions over and over again? Tired of typos coming up in your reports? Faraday provides a simple solution; unify criteria for naming vulnerabilities and save time and effort to yourself and your team.

Faraday comes with its own [CWE](https://cwe.mitre.org/) Vulnerabilities DB for you to use. This is a simple CSV made using CWE standards and allows you to create vulnerabilities without worrying about finding references, description, etc.

To upload it to CouchDB go to your Faraday installation root directory and run 

```
python helpers/pushCwe.py
```

To add your own put the CSV inside **$FARADAY/data/cwe.csv**. Make sure you run the **pushCwe.py** script before use and that's it!