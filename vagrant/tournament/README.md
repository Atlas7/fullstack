# Create the database

Navigate to /vagrant/tournament and issue:

```
psql
```

Once you are in the interactive inline SQL mode (under vagrant database), issue this to create the database `tournament`.

```
CREATE DATABASE tournament;
```

Now the database is created. We need to built up the skeleton tables and views.

Issue this to exit PSQL mode:

```
\q
```

# Create tables and views

Navigate to /vagrant/tournament and log into the newly created `tournament` database.

```
psql tournament
```

Submit the following to create skeleton tables and views.

```
\i tournament.sql
```

Now all the tables and views are built. We are ready to do downstream insert and drop rows, etc.
