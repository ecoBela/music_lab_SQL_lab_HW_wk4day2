import pdb
from models.album import Album
import repositories.album_repository as album_repository

album_repository.delete_all()

album1 = Album("Cruelty and the Beast", "Cradle of Filth", "Metal" )
album_repository.save(album1)
