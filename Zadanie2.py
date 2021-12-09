import unittest
from Zadanie1 import Note
from unittest.mock import *


class NoteStorage:
    def add(self, note):
        pass

    def clear(self):
        pass

    def getAllNotesOf(self, name):
        pass

class NoteService:
    def __init__(self):
        self.noteStorage = NoteStorage()

    def add(self, note):
        return self.noteStorage.add(note)

    def averageOf(self, name):
        allNotes = self.noteStorage.getAllNotesOf(name)
        noteSum = 0
        for note in allNotes:
            noteSum+=note.note
        numOfNotes = len(allNotes)
        if numOfNotes == 0:
            return 0
        return noteSum / numOfNotes

    def clear(self):
        return self.noteStorage.clear()

class NoteServiceTest(unittest.TestCase):
    
    @patch.object(NoteStorage, 'add')
    def test_note_service_add(self, mock_method):
        noteService = NoteService()
        note = Note("note", 3.21)
        mock_method.return_value = True
        self.assertEqual(noteService.add(note), True)
        
    @patch.object(NoteStorage, 'getAllNotesOf')
    def test_averageOf_many_notes(self, mock_method):
        noteService = NoteService()
        mock_method.return_value = [Note("note", 3.0), Note("note", 5.0), Note("note", 2.0), Note("note", 2.0)]
        self.assertEqual(noteService.averageOf("note"), 3.0)

    @patch.object(NoteStorage, 'getAllNotesOf')
    def test_averageOf_one_note(self, mock_method):
        noteService = NoteService()
        mock_method.return_value = [Note("note", 3.0)]
        self.assertEqual(noteService.averageOf("note"), 3.0)
        
    @patch.object(NoteStorage, 'getAllNotesOf')
    def test_averageOf_no_notes(self, mock_method):
        noteService = NoteService()
        mock_method.return_value = []
        self.assertEqual(noteService.averageOf("note"), 0.0)
        
    @patch.object(NoteStorage, "clear")
    def test_clear(self, mock_method):
        noteService = NoteService()
        mock_method.return_value = None
        self.assertIsNone(noteService.clear())
