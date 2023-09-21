import json

class NotesRepository():

    def __init__(self):
        self.path = r"notes\data\notes.json"
        self.notes = self.readNotes()
        

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

        return self.notes
    
    def getText(self, title):
         for note in self.notes:
            if title == note["title"]:
                return note["text"]

    def updateNote(self, title, text):
        for note in self.notes:
            if title == note["title"]:
                note["text"] = text
        
        self.saveFile()

    def deleteNote(self, title):
        for note in self.notes:
            if title == note["title"]:
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