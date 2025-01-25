# test_save_and_load_notes.py Тест сохранения в файл и загрузки из файла
import unittest
from stage_5.data.save_notes_json import save_notes_json
from stage_5.data.load_notes_from_file import load_notes_from_file

class TestNoteManager(unittest.TestCase):
    def test_save_and_load_notes(self):
        notes = [{'username': 'Test', 'title': 'Test Note'}]
        save_notes_json(notes, 'test.json')
        loaded_notes = load_notes_from_file('test.json')
        self.assertEqual(notes, loaded_notes)

if __name__ == '__main__':

    unittest.main()
    # notes = [{'username': 'Test', 'title': 'Test Note'}]
    # save_notes_json(notes, 'test.json')
    # loaded_notes = load_notes_from_file('test.json')
    # print(notes)
    # print(loaded_notes)