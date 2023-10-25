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

    def addTag(self, noteTitle, tag):
        for note in self.notes:
            if note["title"] == noteTitle:
                note["tags"].append(tag)

        self.saveFile()

    def readTags(self, noteTitle):
        for note in self.notes:
            if note["title"] == noteTitle:
                return note["tags"]
    
    def deleteTag(self, noteTitle, tag):
        for note in self.notes:
            if note["title"] == noteTitle:
                note["tags"].remove(tag)

        self.saveFile()

    def searchByTag(self, searchTag):
        filteredNotes = []
        for note in self.notes:
            for tag in note["tags"]:
                if tag == searchTag:
                    filteredNotes.append(note)

        return filteredNotes