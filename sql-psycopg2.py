# Importing the framework
import psycopg2

# Connecting the pyscopg2 framework to the database
connection = psycopg2.connect(database="chinook")

# A list - Like an array in js. Anything that was queried from the database
# becomes part of this list allowing us to loop over data
cursor = connection.cursor()

# Perfoming our query data selections using the execute method and cursor var
# cursor.execute('SELECT * FROM "Artist"')

# cursor.execute('SELECT "Artist" FROM "Artist"')
# cursor.execute('SELECT "Name" FROM "Artist"')
# cursor.execute('SELECT "ArtistID" FROM "Artist"')

# When searching for a specific piece of data such as a name. We need to use
# a Sting placeholder '%s' and place the name into ["name"].
# Ensuring they are seperated by a comma. You can also add as many
# search criteria as you want to, seperated by commas.

cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# As its an integer we do not need to add the quotes to the string.
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', [51])


""" 
Using the cursor.execute method allows us to put out query seach into the
double brackets. But ensuring to wrap the string into '' and any search
paramaters in the "". This is due to the psycopg framework.

Using the * selector is a select all method. Which will select all data
avaliable from the database. Same in other languages too
"""

# Fetching the data from the database (Multiple)
# results = cursor.fetchall()  # Fetching all the data

# Fetching a single data object
results = cursor.fetchone()  # Fetches a single peice of data

# Once the data has been fetched and stored we need to end the connection
connection.close()  # Which closes the connection

# Printing the resulsts out. Once they have been iterated over
for result in results:
    print(result)
