import json

class NotesRepository():

    def __init__(self):
        self.notes = self.readNotes()
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
            self.notes = json.load(file)

        return self.notes

    def updateNote(self, id, updateNote):
        for note in self.notes:
            if id == note["id"]:
                note["title"] = updateNote.title
                note["text"] = updateNote.text
                note["tags"] = updateNote.tags
        
        self.saveFile()

    def deleteNote(self, id):
        for note in self.notes:
            if id == note["id"]:
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