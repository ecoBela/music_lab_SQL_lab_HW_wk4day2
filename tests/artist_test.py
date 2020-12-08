import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Beyonce", 1)
    
    def test_artist_has_name(self):
        self.assertEqual("Beyonce", self.artist.name)
    
    def test_artist_has_id(self):
        self.assertEqual(1, self.artist.id)
