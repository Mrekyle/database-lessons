"""
To run the basic sql server using the command 'psql' will run the basic database

psql -d {name} - Allows an instant connection to a specific database
\q - quits the sql server. Taking us back to the reguler terminal
\l - Shows all the databases avaliable 
\c - connects the database '\c chinook' will connect to that database
\i {file name} - will populate the database with the contents of the file. Into the database that you are connected to. 
\dt - shows the contents of the database that you are connected to 
q - on its own will quit the query seach that was done. Not using the '\' which quits the server
CREATE DATABASE {NAME}; - Creates a new database
SELECT * FROM "{name}"; - Selects all data from the specified table
SELECT "{name}" FROM "{name}"; - selects specific data that has been requested from the table
SELECT * FROM "{name} WHERE "{name}" = "{name}"; - Will select a certain string of data from where it lives such as
    SELECT * FROM "Artist" WHERE "Name" = 'Queen'; - Will select all data from the artist table that is related to queen. Using the single quotes means thats what is being searched for 
"""
