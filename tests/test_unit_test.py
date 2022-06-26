import unittest
from main import YaUploader


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        with open('../tokenYaD.txt', 'r') as file_object:
            tokenYaD = file_object.read().strip()
        self.uploader = YaUploader(tokenYaD)

    def tearDown(self) -> None:
        ...

    @classmethod
    def setUpClass(cls) -> None:
        ...

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    # Папка успешно создана
    def test_new_folder_success(self):
        result = 201
        self.assertEqual(self.uploader.new_folder('NewFolder/'), result)

    # Папка уже существует
    def test_new_folder_already_exist(self):
        result = 409
        self.assertEqual(self.uploader.new_folder('NewFolder/'), result)

    # Папка есть в директории
    def test_new_folder_exist(self):
        result = 200
        self.assertEqual(self.uploader.folders_exist('NewFolder/'), result)

    # Папки нет в директории
    def test_new_folder_not_exist(self):
        result = 404
        self.assertEqual(self.uploader.folders_exist('NewFolder/'), result)