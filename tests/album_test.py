import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.album = Album("Lemonade", "Beyonce", "Pop", 1)
    
    def test_album_has_title(self):
        self.assertEqual("Lemonade", self.album.title)

    def test_album_has_artist(self):
        self.assertEqual("Beyonce", self.album.artist)

    def test_album_has_genre(self):
        self.assertEqual("Pop", self.album.genre)
    
    def test_album_has_id(self):
        self.assertEqual(1, self.album.id)