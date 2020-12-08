from db.run_sql import run_sql
from models.album import Album




# Create and Save Albums  (REMEMBER TO CREATE YOUR OBEJECTS!)
def save(album):
    sql = "INSERT INTO albums (title, artist, genre, id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [album.title, album.artist, album.genre, album.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


# Delete all Albums
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

# Find Albums by their ID (select)
def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

if result is not None:
    album = Album(result['title'], result['artist'], result['genre'], result['id'])
return album

# List All Artists/Albums (select_all)

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

for row in results:
    album = Album(row['title'], row['artist'], row['genre'])