from unittest import mock
from unittest.mock import Mock, call, mock_open, patch
import unittest
from Zadanie1.FileEdit import FileEdit


class TestFileEdit(unittest.TestCase):

    def setUp(self):
        self.temp = FileEdit()

    def test_open_file(self):
        file_path = "plik.txt"
        mock = mock_open(read_data="abc")
        with patch('builtins.open', mock):
            self.assertEqual(self.temp.open_file(file_path), "abc")


    def test_edit_file(self):
        file_path = "plik.txt"
        # text = "def"
        mock = mock_open(read_data="abc")
        with patch('builtins.open', mock):
            self.temp.edit_file(file_path, "def")
        mock.assert_called_once_with(file_path, "w")

    @mock.patch('Zadanie1.FileEdit.os.path')
    @mock.patch('Zadanie1.FileEdit.os')
    def test_delete_file(self, mock_os, mock_path):
        file_path = "plik.txt"
        mock_path.exists.return_value = True
        self.temp.delete_file(file_path)
        mock_os.remove.assert_called_with(file_path)


    def tearDown(self):
        self.temp = None



if __name__ == '__main__':
    unittest.main()