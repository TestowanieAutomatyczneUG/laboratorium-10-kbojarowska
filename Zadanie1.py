import unittest

class Note:
    def __init__(self, name, note):
        if name is None:
            raise Exception("Name can't be null")
        elif type(name) is not str:
            raise Exception("Name must be str")
        elif len(name)==0:
            raise Exception("Length of name can't be 0")
        elif type(note) is not float:
            raise Exception("Note must be float")
        elif not 2<= note <=6:
            raise Exception("Note must be between 2 and 6")
        self.name = name
        self.note = note

    def getName(self):
        return self.name
    
    def getNote(self):
        return self.note

class NoteTest(unittest.TestCase):
    def setUp(self):
        self.temp = Note("abcd", 4.32)

    def test_bad_name_int(self):
        with self.assertRaisesRegex(Exception, "Name must be str"):
            Note(3, 5.43)

    def test_bad_name_dict(self):  
        with self.assertRaisesRegex(Exception, "Name must be str"):
            Note({}, 5.43)

    def test_bad_name_list(self):
        with self.assertRaisesRegex(Exception, "Name must be str"):
            Note([], 5.43)

    def test_bad_name_empty_str(self):
        with self.assertRaisesRegex(Exception, "Length of name can't be 0"):
            Note("", 5.43)

    def test_bad_note_int(self):
        with self.assertRaisesRegex(Exception, "Note must be float"):
            Note("abcd", 3)

    def test_bad_note_too_big_int(self):
        with self.assertRaisesRegex(Exception, "Note must be float"):
            Note("abcd", 42)

    def test_bad_note_too_small_int(self):
        with self.assertRaisesRegex(Exception, "Note must be float"):
            Note("abcd", 0)

    def test_bad_note_too_small_float(self):
        with self.assertRaisesRegex(Exception, "Note must be between 2 and 6"):
            Note("abcd", 1.431)

    def test_bad_note_too_big_float(self):
        with self.assertRaisesRegex(Exception, "Note must be between 2 and 6"):
            Note("abcd", 42.32)

    def test_bad_note_str(self):
        with self.assertRaisesRegex(Exception, "Note must be float"):
            Note("abcd", "")

    def test_bad_note_dict(self):
        with self.assertRaisesRegex(Exception, "Note must be float"):
            Note("abcd", {})
    
    def test_bad_note_list(self):
        with self.assertRaisesRegex(Exception, "Note must be float"):
            Note("abcd", [])

    def test_bad_note_tuple(self):
        with self.assertRaisesRegex(Exception, "Note must be float"):
            Note("abcd", ())

    def test_get_name(self):
        self.assertEqual("abcd", self.temp.getName())

    def test_get_note(self):
        self.assertEqual(4.32, self.temp.getNote())   
