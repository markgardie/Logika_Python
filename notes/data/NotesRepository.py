import json

class NotesRepository():

    def __init__(self):
        self.notes = []
        self.path = r"D:\Mark\Desktop\Logika_Python\notes\data\notes.json"

    def saveFile(self):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(self.notes, file)

    def createNote(self, newNote):
        self.notes.append(newNote)
        self.saveFile()
        pass

    def readNotes(self):
        with open(self.path, "r", encoding="utf-8") as file:
            self.notes = json.load(file)

    def updateNote(self, noteTitle, noteText):
        for note in self.notes:
            if note["title"] == noteTitle:
                note["text"] = noteText
        
        self.saveFile()

    def deleteNote(self, noteTitle):
        for note in self.notes:
            if note["title"] == noteTitle:
                self.notes.remove(note)

        self.saveFile()

    def addTag(self):
        pass

    def readTags(self):
        pass

    def deleteTag(self):
        pass

    def searchByTag(self):
        pass