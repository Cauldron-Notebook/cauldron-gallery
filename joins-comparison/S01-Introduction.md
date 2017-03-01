# SQL vs SQLAlchemy vs Pandas Joins

We're going to look at the syntactical differences of simple joins in SQL,
SQLAlchemy's Expression Language and in Pandas data frames. For these examples
we're going to use the familiar AutoMPG data set. However, we're going to
break it into two tables **attributes** and **performance**, which will
share a *name* column that will be used for the joins.

Before we get to the joins we need to load and transform the raw CSV data
set into Pandas data frames as well as populating an SQLite in-memory database
containing those tables.
