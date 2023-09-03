import json

class NotesRepository():

    def __init__(self):
        self.notes = []
        self.path = r"D:\Mark\Desktop\Logika_Python\notes\data\notes.json"

    def saveFile(self):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(self.notes)

    def createNotes(self, newNote):
        self.notes.append(newNote.__dict__)
        self.saveFile()
        pass

    def readNotes(self):
        with open(self.path, "r", encoding="utf-8") as file:
            self.notes = file.read()

    def updateNote(self):
        pass

    def deleteNote(self):
        pass

    def addTag(self):
        pass

    def readTags(self):
        pass

    def deleteTag(self):
        pass

    def searchByTag(self):
        pass