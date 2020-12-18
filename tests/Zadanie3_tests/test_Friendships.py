import unittest
from Zadanie3.Friendships import Friendships
from unittest.mock import *
from unittest.mock import MagicMock

class TestNote(unittest.TestCase):

    def setUp(self):
        self.temp = Friendships()

    def test_get_friends_list_nowak(self):
        frListNowak = ["Miotk", "Kowalski", "Bobkowska"]
        self.assertEqual(self.temp.getFriendsList("Nowak"), frListNowak)

    def test_get_friends_list_kowalski(self):
        frListKowalski = ["Miotk", "Nowak"]
        self.assertEqual(self.temp.getFriendsList("Kowalski"), frListKowalski)

    def test_get_friends_list_kowalski_called_once(self):
        mock = Friendships()
        mock.getFriendsList = MagicMock()
        mock.getFriendsList("Kowalski")
        mock.getFriendsList.assert_called_once_with("Kowalski")

    def test_are_friends_nowak_kowalski(self):
        mock = Friendships()
        mock.areFriends = MagicMock()
        mock.areFriends("Nowak", "Kowalski")
        mock.areFriends.assert_called_once_with("Nowak", "Kowalski")

    def test_add_friend_nowak(self):
        mock = Friendships()
        mock.addFriend = MagicMock()
        mock.addFriend("Nowak", "Kowalska")
        mock.addFriend.assert_called_once_with("Nowak", "Kowalska")

    def test_make_friends_kowalski_bobkowska(self):
        mock = Friendships()
        mock.makeFriends = MagicMock()
        mock.makeFriends("Kowalski", "Bobkowska")
        mock.makeFriends.assert_called_once_with("Kowalski", "Bobkowska")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
