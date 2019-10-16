# Remote PostgreSQL configuration

Faraday uses a connection string stored in /home/faraday/.faraday/config/server.ini to connect to the database.
You can use `faraday-manage initdb` to configure a localhost database (same server as faraday runs).
If you opt to use a remote database you will need to create a database role, database and create the schema.

# Step 1: Configure PostgreSQL for remote connection

WARNING! Make sure you understand this step. Using the wrong settings could leave your database server insecure

First open the hba_config file, to locate the file execute:

```
sudo -u postgres psql -c "show hba_file"
```

Add a line for the faraday-server

```
host    all             all             192.168.1.2/24            md5
```

Then open `/etc/postgresql/9.X/main/postgresql.conf 

Allow to listen on the interface or use `*` for all interfaces:

```
listen_addresses = '*'
```


# Step 2: Create PostgreSQL role

Login into the database server and execute:

```
createuser faraday_postgresql -P
```

Now create the database:

```
createdb faraday
```

# Step 3: Configure faraday server

Now on the faraday server instance, open the file `/home/faraday/.faraday/config/server.ini` and append the database configuration:

```
[database]
connection_string = postgresql+psycopg2://faraday_postgresql:SECRET_PASSWORD@REMOTE_IP/faraday
```

# Step 4: Create tables

Now you are ready to create the tables:

```
faraday-manage create-tables
```