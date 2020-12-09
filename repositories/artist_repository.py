from db.run_sql import run_sql
from models.artist import Artist


# Create and Save Artists

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


# Delete all Artists

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)
# Find Artists by their ID (select)
# List All Artists (select_all)



