import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()

album1 = Album("Cruelty and the Beast", "Cradle of Filth", "Metal" )
album_repository.save(album1)

artist1 = Artist("Cradle of Filth")
artist_repository.save(artist1)
