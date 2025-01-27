# test_save_and_load_notes.py Тест сохранения в файл и загрузки из файла
import unittest
from data.save_notes_to_file import save_notes_to_file
from data.load_notes_from_file import load_notes_from_file

class TestNoteManager(unittest.TestCase):
    def test_save_and_load_notes(self):
        notes = [
        {'username': 'Test name', 'title': 'Test title', 'content': 'Test content',
         'status': 'новая', 'created_date': '2025-1-10', 'issue_date': '2025-1-30'}]
        save_notes_to_file(notes, 'test.txt')
        loaded_notes = load_notes_from_file('test.txt')
        self.assertEqual(notes, loaded_notes)

if __name__ == '__main__':

    unittest.main()