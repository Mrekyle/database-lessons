from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

"""
The ending is what is linking the application to the sql database
The reason for tje 3 '/' is telling alchemy that the server is hosted
locally
"""
db = create_engine("postgresql:///chinook")

# Storing the data from the tables in the database inside of the meta
meta = MetaData(db)

# Artist Meta Table
"""
Telling the table var what columns are to be expected inside of the table
by defining what the Columns are and what the value that is to be 
expected inside of the table by the application/server
"""
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.Artistid"))
)

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)


# Conecting to the database using the .connect method and storing it in
# connection
with db.connect() as connection:

    """
    .select method allows us to select the certain table variable that 
    we are trying to build out and display in the console using the 
    print method. 
    Will print out each table to the console
    """
    # select_query = artist_table.select()
    # select_query = album_table.select()
    # select_query = track_table.select()

    """
    Selecting a specific column from the table.
    Using the with_only_columns method allows us to select a certain column
    using the .c method selects the certain column that was required
    """

    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    """
    Selecting a specific value from the table
    Almost the same as selecting a certain column. But instead using the .where
    method to locate a certain name on the table where it is equal to Queen
    """

    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    """
    Almost the exact same as selecting the artist id too
    Just inserting an integer instead of string into the search critera
    """

    # select_query = artist_table.select().where(artist_table.c.ArtistID == 51)

    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    """
    Using the execute method on the connection variable lea
    we call to the server to get the values and store them in a 
    results variable. Then by looping over the results we build the 
    table out to display it to the terminal
    """
    results = connection.execute(select_query)
    for result in results:  # Looping over the results from the tables
        print(result)
