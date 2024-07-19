# Introduction
Hi! This is a very simple backend project that allows for the creation of users and posts, with the programs being used including Python, Postgres/pgAdmin 4, and Postman (for testing).

# Setup
The Python modules used for this tasks were Flask, secrets, psycopg2, requests, and pytest. With the database, I've added a .sql file with queries that should allow you to set up the data quickly with some extra queries that are useful if doing any extra testing with the APIs. If the credentials are the same as the defaults given when installing Postgres, edits to any of the files shouldn't be necessary (like with the base URL, ports, username, password, etc).

# Testing
I used Postman to test all of the APIs individually, and I included a couple of tests in the pytest file just to cover the two tables.

# Thought Process
To keep things super simple and mitigate any worries of appropriate scaling, I made the tables and queries basic with only the necessary categories, such as the username, password, id, etc. With extra time, I would've also added in extra features like creation date, first/last name, and hashing/encryption as well as more rigourous testing both in terms of unit tests and authentication verification. The one thing I would note with the tables is that both primary key id's are an IDENTITY column and would auto-increment upon creation; there are other methods to auto-increment the id's that are most likely more efficient.
